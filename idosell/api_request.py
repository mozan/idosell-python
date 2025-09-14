from __future__ import annotations
from enum import Enum

from typing import Any, Dict, Optional

import httpx
from pydantic import BaseModel

from idosell._common import Gateway

class ApiRequest:
    def __init__(self,
        base_url: Optional[str] = None, # Required if 'client' doesn't have a base_url
        client: Optional[httpx.Client] = None, # Optional httpx.Client; if not provided, a temporary one is created
        headers: Optional[Dict[str, str]] = None, # Extra headers or httpx.Auth
        auth: Optional[httpx.Auth] = None, #  Extra headers or httpx.Auth
        bearer_token: Optional[str] = None, # Convenience auth options
        api_key: Optional[str] = None, # Convenience auth options
        api_key_header: str = "X-API-KEY",
        timeout: Optional[float | httpx.Timeout] = None # float or httpx.Timeout
    ):
        self.base_url = base_url
        self.client = client
        self.config: Dict[str, Any] = {
            'headers': headers,
            'auth': auth,
            'bearer_token': bearer_token,
            'api_key': api_key,
            'api_key_header': api_key_header,
            'timeout': timeout
        }

    def _encode_query_value(self, value: Any) -> Any:
        # Enums -> their value, lists/sets/tuples -> comma-separated, bools -> "true"/"false"
        if isinstance(value, Enum):
            return value.value
        if isinstance(value, (list, tuple, set)):
            return ",".join(str(self._encode_query_value(v)) for v in value) # type: ignore
        if isinstance(value, bool):
            return "true" if value else "false"
        return value

    def _build_query_params(self, model: BaseModel) -> Dict[str, Any]:
        # Prefer model's custom builder if present
        build_q = getattr(model, "build_query", None)
        if callable(build_q):
            params = build_q()
            # Ensure final encoding
            return {k: self._encode_query_value(v) for k, v in params.items() if v is not None}  # type: ignore

        # Generic pydantic v2 dump with aliases for camelCase
        data = model.model_dump(by_alias=True, exclude_none=True)
        return {k: self._encode_query_value(v) for k, v in data.items()}

    def _merge_headers(
        self,
        headers: Optional[Dict[str, str]],
        bearer_token: Optional[str],
        api_key: Optional[str],
        api_key_header: str,
    ) -> Dict[str, str]:
        final = {
            "Accept": "application/json",
            "User-Agent": "idosell-python-httpx",
        }
        if headers:
            final.update(headers)
        if bearer_token:
            final["Authorization"] = f"Bearer {bearer_token}"
        if api_key:
            final[api_key_header] = api_key
        return final

    def request(
        self,
        dto: Gateway,
        raise_for_status: bool = False,
        parse_json: bool = True,
        *,
        base_url: Optional[str] = None,
        client: Optional[httpx.Client] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[httpx.Auth] = None,
        bearer_token: Optional[str] = None,
        api_key: Optional[str] = None,
        api_key_header: str = "X-API-KEY",
        timeout: Optional[float | httpx.Timeout] = None,
    ) -> Any:
        """
        Generic GET request for Gateway-based DTOs.

        - dto: Pydantic model with `_endpoint` and optional `_method` (defaults to GET)
        - base_url: Required if `client` doesn't have a base_url
        - client: Optional httpx.Client; if not provided, a temporary one is created
        - headers/auth: Extra headers or httpx.Auth
        - bearer_token/api_key: Convenience auth options
        - timeout: float or httpx.Timeout
        - raise_for_status: If True, raises on 4xx/5xx
        - parse_json: If True, returns response.json(); otherwise returns httpx.Response
        """

        method = getattr(dto, "_method", "GET").upper()
        endpoint = getattr(dto, "_endpoint", None)
        if not endpoint:
            raise ValueError("DTO must define a private '_endpoint' attribute")

        # Build query params and/or JSON body
        json_body: Any = None
        params: Optional[Dict[str, Any]] = None

        if method in {"GET", "HEAD"}:
            params = self._build_query_params(dto)
        else:
            # Allow DTO to provide custom query params even for non-GET
            build_q = getattr(dto, "build_query", None)
            if callable(build_q):
                q = build_q()
                params = {k: self._encode_query_value(v) for k, v in q.items() if v is not None}  # type: ignore
            # Prefer DTO-provided body if present; otherwise dump the DTO as JSON
            build_b = getattr(dto, "build_body", None)
            if callable(build_b):
                json_body = build_b()
            else:
                json_body = dto.model_dump(by_alias=True, exclude_none=True)

        ak = api_key or self.config['api_key']
        req_headers = self._merge_headers(headers or self.config['headers'], bearer_token or self.config['bearer_token'], ak, api_key_header or self.config['api_key_header'])

        owns_client = client is None
        if client is None:
            base = base_url or self.base_url
            if not base:
                raise ValueError("base_url is required when no client is provided")
            client = httpx.Client(base_url=base, timeout=timeout or self.config['timeout'])
        try:
            if method == "GET":
                resp = client.request(
                    method = method,
                    url = endpoint,  # resolved against base_url if set on client
                    params = params, # type: ignore
                    json = json_body, # type: ignore
                    headers = req_headers,
                    auth = auth or self.config['auth'],
                    timeout = timeout or self.config['timeout'],
                )
                if raise_for_status:
                    resp.raise_for_status()
                else:
                    if resp.is_error:
                        if parse_json:
                            return {
                                "_error": {
                                    "status_code": resp.status_code,
                                    "reason": resp.reason_phrase,
                                    "url": str(resp.request.url),
                                    "body": resp.text,
                                }
                            }
                        return resp

                return resp.json() if parse_json else resp
        finally:
            if owns_client:
                client.close()

    async def async_request(
        self,
        dto: Gateway,
        raise_for_status: bool = False,
        parse_json: bool = True,
        *,
        base_url: Optional[str] = None,
        client: Optional[httpx.AsyncClient] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[httpx.Auth] = None,
        bearer_token: Optional[str] = None,
        api_key: Optional[str] = None,
        api_key_header: str = "X-API-KEY",
        timeout: Optional[float | httpx.Timeout] = None,
    ) -> Any:
        """
        Async variant of get_request using httpx.AsyncClient.
        """

        method = getattr(dto, "_method", "GET").upper()
        endpoint = getattr(dto, "_endpoint", None)
        if not endpoint:
            raise ValueError("DTO must define a private '_endpoint' attribute")

        # Build query params and/or JSON body
        json_body: Any = None
        params: Optional[Dict[str, Any]] = None

        if method in {"GET", "HEAD"}:
            params = self._build_query_params(dto)
        else:
            # Allow DTO to provide custom query params even for non-GET
            build_q = getattr(dto, "build_query", None)
            if callable(build_q):
                q = build_q()
                params = {k: self._encode_query_value(v) for k, v in q.items() if v is not None}  # type: ignore
            # Prefer DTO-provided body if present; otherwise dump the DTO as JSON
            build_b = getattr(dto, "build_body", None)
            if callable(build_b):
                json_body = build_b()
            else:
                json_body = dto.model_dump(by_alias=True, exclude_none=True)

        ak = api_key or self.config['api_key']
        req_headers = self._merge_headers(headers or self.config['headers'], bearer_token or self.config['bearer_token'], ak, api_key_header or self.config['api_key_header'])

        owns_client = client is None
        if client is None:
            base = base_url or self.base_url
            if not base:
                raise ValueError("base_url is required when no client is provided")
            client = httpx.AsyncClient(base_url=base, timeout=timeout or self.config['timeout'])
        try:
            resp = await client.request(
                method = method,
                url = endpoint,
                params = params, # type: ignore
                json = json_body, # type: ignore
                headers = req_headers,
                auth = auth or self.config['auth'],
                timeout = timeout or self.config['timeout'],
            )
            if raise_for_status:
                resp.raise_for_status()
            else:
                if resp.is_error:
                    if parse_json:
                        return {
                            "_error": {
                                "status_code": resp.status_code,
                                "reason": resp.reason_phrase,
                                "url": str(resp.request.url),
                                "body": resp.text,
                            }
                        }
                    return resp

            return await resp.json() if parse_json else resp
        finally:
            if owns_client:
                await client.aclose()
