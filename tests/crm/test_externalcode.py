import pytest
from pydantic import ValidationError

from src.idosell.crm.externalcode import (
    PutCrmExternalcodeParamsModel,
    Put
)


# --- Tests for DTOs
class TestPutCrmExternalcodeParamsModel:
    def test_valid(self):
        dto = PutCrmExternalcodeParamsModel(
            client_id=100,
            client_login="john.doe",
            code_extern="EXT12345"
        )
        assert dto.client_id == 100
        assert dto.client_login == "john.doe"
        assert dto.code_extern == "EXT12345"

    def test_invalid_client_id_zero(self):
        with pytest.raises(ValidationError):
            PutCrmExternalcodeParamsModel(
                client_id=0,
                client_login="test",
                code_extern="CODE"
            )

    def test_invalid_client_id_negative(self):
        with pytest.raises(ValidationError):
            PutCrmExternalcodeParamsModel(
                client_id=-1,
                client_login="test",
                code_extern="CODE"
            )

    def test_invalid_client_login_empty(self):
        with pytest.raises(ValidationError):
            PutCrmExternalcodeParamsModel(
                client_id=1,
                client_login="",
                code_extern="CODE"
            )

    def test_invalid_code_extern_empty(self):
        with pytest.raises(ValidationError):
            PutCrmExternalcodeParamsModel(
                client_id=1,
                client_login="test",
                code_extern=""
            )


# --- Tests for Endpoints
class TestPut:
    def test_instantiate(self):
        dto = Put(
            params=PutCrmExternalcodeParamsModel(
                client_id=200,
                client_login="jane.smith",
                code_extern="EXT67890"
            )
        )
        assert hasattr(dto, '_method')
        assert hasattr(dto, '_endpoint')
        assert dto.params.client_id == 200
        assert dto.params.client_login == "jane.smith"
        assert dto.params.code_extern == "EXT67890"

    def test_method_is_put(self):
        dto = Put(
            params=PutCrmExternalcodeParamsModel(
                client_id=1,
                client_login="test",
                code_extern="CODE"
            )
        )
        assert dto._method == 'PUT'

    def test_endpoint_correct(self):
        dto = Put(
            params=PutCrmExternalcodeParamsModel(
                client_id=1,
                client_login="test",
                code_extern="CODE"
            )
        )
        assert dto._endpoint == '/api/admin/v6/clients/externalCode'
