import pytest
from pydantic import ValidationError

from src.idosell.crm.newsletter import (
    SearchEmailCrmNewsletterParamsModel, SearchSmsCrmNewsletterParamsModel,
    SearchEmail, SearchSms
)
from src.idosell.crm._common import DateModel, ShopsModel
from src.idosell._common import BooleanStrShortEnum


# --- Tests for DTOs
class TestSearchEmailCrmNewsletterParamsModel:
    def test_valid_minimal(self):
        dto = SearchEmailCrmNewsletterParamsModel()
        assert dto.shops is None
        assert dto.language is None
        assert dto.date is None

    def test_valid_with_shops(self):
        dto = SearchEmailCrmNewsletterParamsModel(
            shops=[
                ShopsModel(shop_id=1, approval=BooleanStrShortEnum.YES, registered=BooleanStrShortEnum.YES)
            ]
        )
        assert len(dto.shops) == 1
        assert dto.shops[0].shop_id == 1

    def test_valid_with_language(self):
        dto = SearchEmailCrmNewsletterParamsModel(language="eng")
        assert dto.language == "eng"

    def test_valid_with_date(self):
        dto = SearchEmailCrmNewsletterParamsModel(
            date=DateModel(**{"from": "2023-01-01 00:00:00"}, to="2023-12-31 23:59:59")
        )
        assert dto.date.to == "2023-12-31 23:59:59"

    def test_valid_with_return_elements(self):
        dto = SearchEmailCrmNewsletterParamsModel(
            return_elements=["clientEmail", "clientNewsletter"]
        )
        assert len(dto.return_elements) == 2

    def test_invalid_shops_empty(self):
        with pytest.raises(ValidationError):
            SearchEmailCrmNewsletterParamsModel(shops=[])

    def test_invalid_language_empty(self):
        with pytest.raises(ValidationError):
            SearchEmailCrmNewsletterParamsModel(language="")

    def test_invalid_return_elements_empty(self):
        with pytest.raises(ValidationError):
            SearchEmailCrmNewsletterParamsModel(return_elements=[])

class TestSearchSmsCrmNewsletterParamsModel:
    def test_valid_minimal(self):
        dto = SearchSmsCrmNewsletterParamsModel()
        assert dto.shops is None
        assert dto.language is None

    def test_valid_with_shops(self):
        dto = SearchSmsCrmNewsletterParamsModel(
            shops=[
                ShopsModel(shop_id=2, approval=BooleanStrShortEnum.NO, registered=BooleanStrShortEnum.NO)
            ]
        )
        assert len(dto.shops) == 1
        assert dto.shops[0].approval == BooleanStrShortEnum.NO

    def test_valid_with_all_fields(self):
        dto = SearchSmsCrmNewsletterParamsModel(
            shops=[ShopsModel(shop_id=1, approval=BooleanStrShortEnum.YES, registered=BooleanStrShortEnum.YES)],
            language="pol",
            date=DateModel(**{"from": "2023-01-01 00:00:00"}, to="2023-12-31 23:59:59"),
            return_elements=["clientPhone"]
        )
        assert dto.language == "pol"
        assert len(dto.return_elements) == 1


# --- Tests for Endpoints
class TestSearchEmail:
    def test_instantiate_minimal(self):
        dto = SearchEmail(params=SearchEmailCrmNewsletterParamsModel())
        assert hasattr(dto, '_method')
        assert hasattr(dto, '_endpoint')
        assert dto.params.shops is None

    def test_instantiate_with_shops(self):
        dto = SearchEmail(
            params=SearchEmailCrmNewsletterParamsModel(
                shops=[
                    ShopsModel(shop_id=1, approval=BooleanStrShortEnum.YES, registered=BooleanStrShortEnum.YES)
                ]
            )
        )
        assert len(dto.params.shops) == 1

    def test_instantiate_with_full_params(self):
        dto = SearchEmail(
            params=SearchEmailCrmNewsletterParamsModel(
                shops=[ShopsModel(shop_id=1, approval=BooleanStrShortEnum.YES, registered=BooleanStrShortEnum.YES)],
                language="eng",
                date=DateModel(**{"from": "2023-01-01 00:00:00"}, to="2023-12-31 23:59:59"),
                return_elements=["clientEmail"]
            )
        )
        assert dto.params.language == "eng"

class TestSearchSms:
    def test_instantiate_minimal(self):
        dto = SearchSms(params=SearchSmsCrmNewsletterParamsModel())
        assert hasattr(dto, '_method')
        assert hasattr(dto, '_endpoint')
        assert dto.params.shops is None

    def test_instantiate_with_shops(self):
        dto = SearchSms(
            params=SearchSmsCrmNewsletterParamsModel(
                shops=[
                    ShopsModel(shop_id=2, approval=BooleanStrShortEnum.NO, registered=BooleanStrShortEnum.YES)
                ]
            )
        )
        assert len(dto.params.shops) == 1
        assert dto.params.shops[0].shop_id == 2

    def test_instantiate_with_full_params(self):
        dto = SearchSms(
            params=SearchSmsCrmNewsletterParamsModel(
                shops=[ShopsModel(shop_id=3, approval=BooleanStrShortEnum.YES, registered=BooleanStrShortEnum.NO)],
                language="pol",
                date=DateModel(**{"from": "2023-06-01 00:00:00"}, to="2023-06-30 23:59:59"),
                return_elements=["clientPhone", "clientNewsletter"]
            )
        )
        assert dto.params.language == "pol"
        assert len(dto.params.return_elements) == 2
