import os
import sys
from typing import Any
from pathlib import Path
from dotenv import load_dotenv

# Add the project root to the Python path BEFORE imports
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from src.idosell.api_request import ApiRequest
from samples.cms_dtos import cms_delete, cms_get, cms_post, cms_put
from samples.crm_dtos import crm_delete, crm_get, crm_post, crm_put, crm_search
from samples.oms_dtos import oms_delete, oms_get, oms_post, oms_put, oms_search
from samples.pim_dtos import pim_delete, pim_get, pim_post, pim_put
from samples.pim_products_dtos import pim_products_delete, pim_products_get, pim_products_post, pim_products_put, pim_products_search
from samples.system_dtos import system_delete, system_get, system_post, system_put
from samples.wms_dtos import wms_delete, wms_get, wms_post, wms_put
from samples.pim_products_product_dtos import pim_products_product_delete, pim_products_product_get, pim_products_product_post, pim_products_product_put, pim_products_product_search

if __name__ == "__main__":
    # Load environment variables from .env files
    load_dotenv(Path(__file__).resolve().parents[1] / ".env.secrets", override = True)

    IDOSELL_BASE_URL = os.getenv("IDOSELL_BASE_URL")
    IDOSELL_API_KEY = os.getenv("IDOSELL_API_KEY")

    api = ApiRequest(base_url = IDOSELL_BASE_URL, api_key = IDOSELL_API_KEY)

    test_delete_dtos: list[Any] = [
        cms_delete, crm_delete, oms_delete, pim_delete, pim_products_delete, pim_products_product_delete, system_delete, wms_delete
    ]
    test_get_dtos: list[Any] = [
        cms_get, crm_get, oms_get, pim_get, pim_products_get, pim_products_product_get, system_get, wms_get
    ]
    test_post_dtos: list[Any] = [
        cms_post,
        crm_post,
        oms_post,
        pim_post,
        pim_products_post,
        pim_products_product_post,
        system_post,
        wms_post
    ]
    test_put_dtos: list[Any] = [
        cms_put,
        crm_put,
        oms_put,
        pim_put,
        pim_products_put,
        pim_products_product_put,
        system_put,
        wms_put
    ]
    test_search_dtos: list[Any] = [
        crm_search, oms_search, pim_products_search, pim_products_product_search
    ]

    test_dtos: list[Any] = [
        # test_delete_dtos,
        test_get_dtos,
        # test_post_dtos,
        # test_put_dtos,
        test_search_dtos
    ]

    # --- TEST DTOS
    for test_dto in test_dtos:
        for dtos in test_dto:
            for d in dtos:
                endpoint = getattr(d, "_endpoint")
                method = getattr(d, "_method", "GET").upper()
                print(method + ": " + endpoint)
                if method == "GET":
                    res = 'test'
                    res = api.request(d)
                    # res = asyncio.run(api.async_request(d))
                    print(method + ": " + endpoint + ":\nresponse:\n", res)
                else:
                    print(method + ": " + endpoint + ":\nSKIPPED (POST/PUT/DELETE)\n")
