import pytest
from pydantic import ValidationError

from src.idosell.crm.provincelist import Get


# --- Tests for Endpoints
class TestGet:
    def test_instantiate_minimal(self):
        dto = Get()
        assert hasattr(dto, '_method')
        assert hasattr(dto, '_endpoint')
        assert dto.country_code is None

    def test_instantiate_with_country_code(self):
        dto = Get(country_code="US")
        assert dto.country_code == "US"

    def test_instantiate_with_lowercase_country_code(self):
        dto = Get(country_code="pl")
        assert dto.country_code == "pl"

    def test_invalid_country_code_too_short(self):
        with pytest.raises(ValidationError):
            Get(country_code="U")

    def test_invalid_country_code_too_long(self):
        with pytest.raises(ValidationError):
            Get(country_code="USA")

    def test_invalid_country_code_with_numbers(self):
        with pytest.raises(ValidationError):
            Get(country_code="U1")

    def test_invalid_country_code_with_special_chars(self):
        with pytest.raises(ValidationError):
            Get(country_code="U$")

    def test_method_is_get(self):
        dto = Get()
        assert dto._method == 'GET'

    def test_endpoint_correct(self):
        dto = Get()
        assert dto._endpoint == '/api/admin/v6/clients/provinceList'
