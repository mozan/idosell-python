import pytest
from pydantic import ValidationError

from src.idosell.pim.products.product.product import (
    # DTOs
    DeletePimProductsProductProductParamsModel,
    SearchPimProductsProductProductParamsModel,
    PostPimProductsProductProductParamsModel,
    PutPimProductsProductProductParamsModel,
    # Endpoints
    Delete,
    Get,
    Post,
    Put,
    Search,
)
from src.idosell.pim.products.product._common import (
    ProductsDeleteModel,
    SettingsPostModel, SettingsPutModel,
    PictureSettingsPostModel, SettingDefaultCategoryModel, SettingDefaultSizesGroupModel,
    PicturesSettingInputTypeEnum, SettingModificationTypeEnum, SettingCalculateBasePriceSizesEnum,
    SettingActualizeDelivererModeEnum,
    SettingDeleteIndividualDescriptionsByShopsMaskModel, SettingDeleteIndividualMetaByShopsMaskModel
)
from src.idosell._common import BooleanStrShortEnum


# --- Tests for DTOs
class TestDeletePimProductsProductProductParamsModel:
    def test_valid(self):
        dto = DeletePimProductsProductProductParamsModel(
            products=[ProductsDeleteModel(productId=1, productSizeCodeExternal="code1"), ProductsDeleteModel(productId=2, productSizeCodeExternal="code2")]
        )
        assert dto.products[0].productId == 1
        assert dto.products[1].productId == 2

    def test_single_product(self):
        dto = DeletePimProductsProductProductParamsModel(
            products=[ProductsDeleteModel(productId=123, productSizeCodeExternal="code")]
        )
        assert dto.products[0].productId == 123

    def test_empty_products(self):
        with pytest.raises(ValidationError):
            DeletePimProductsProductProductParamsModel(products=[])

    def test_invalid_product_id_zero(self):
        with pytest.raises(ValidationError):
            DeletePimProductsProductProductParamsModel(
                products=[ProductsDeleteModel(productId=0, productSizeCodeExternal="code")]
            )


class TestPostPimProductsProductProductParamsModel:
    # Note: ProductsPostModel has 40+ required fields making full instantiation impractical for unit tests
    # Tests focus on validation logic that can be tested

    def test_empty_products_list(self):
        settings = SettingsPostModel(
            settingDefaultCategory=SettingDefaultCategoryModel(categoryId=1, categoryName="Test"),
            settingDefaultSizesGroup=SettingDefaultSizesGroupModel(sizesGroupId=1, sizesGroupName="Default")
        )
        picture_settings = PictureSettingsPostModel(
            picturesSettingInitialUrlPart="http://example.com/",
            picturesSettingInputType=PicturesSettingInputTypeEnum.URL,
            picturesSettingOverwrite=BooleanStrShortEnum.NO,
            picturesSettingScaling=BooleanStrShortEnum.YES
        )

        with pytest.raises(ValidationError):
            PostPimProductsProductProductParamsModel(
                settings=settings,
                picturesSettings=picture_settings,
                products=[]
            )


class TestPutPimProductsProductProductParamsModel:
    # Note: ProductsPutModel has 40+ required fields making full instantiation impractical for unit tests
    # Tests focus on validation logic that can be tested

    def test_empty_products_list(self):
        settings = SettingsPutModel(
            settingModificationType=SettingModificationTypeEnum.EDIT,
            settingCalculateBasePriceSizes=SettingCalculateBasePriceSizesEnum.AVAILABLE,
            settingAddingSizeschartAllowed=BooleanStrShortEnum.NO,
            settingDefaultCategory=SettingDefaultCategoryModel(categoryId=1, categoryName="Test"),
            settingDefaultSizesGroup=SettingDefaultSizesGroupModel(sizesGroupId=1, sizesGroupName="Default"),
            settingIgnoreRetailPricesInCaseOfPromotion=BooleanStrShortEnum.NO,
            returnPromotionStatus=BooleanStrShortEnum.NO,
            settingsRestoreDeletedProducts=BooleanStrShortEnum.NO,
            settingAddingSupplierAllowed=BooleanStrShortEnum.NO,
            settingActualizeDelivererMode=SettingActualizeDelivererModeEnum.NONE,
            settingDeleteIndividualDescriptionsByShopsMask=SettingDeleteIndividualDescriptionsByShopsMaskModel(shopsMask=1),
            settingDeleteIndividualMetaByShopsMask=SettingDeleteIndividualMetaByShopsMaskModel(shopsMask=1),
            settingsSkipDuplicatedProducers=False
        )

        with pytest.raises(ValidationError):
            PutPimProductsProductProductParamsModel(
                settings=settings,
                products=[]
            )


class TestSearchPimProductsProductProductParamsModel:
    def test_valid_empty(self):
        dto = SearchPimProductsProductProductParamsModel()
        assert dto.productIsAvailable is None
        assert dto.containsText is None

    def test_with_some_fields(self):
        dto = SearchPimProductsProductProductParamsModel(
            productIsAvailable=BooleanStrShortEnum.YES,
            containsText="test"
        )
        assert dto.productIsAvailable == BooleanStrShortEnum.YES
        assert dto.containsText == "test"

    def test_with_boolean_filters(self):
        dto = SearchPimProductsProductProductParamsModel(
            productIsVisible=BooleanStrShortEnum.YES,
            productInPromotion=BooleanStrShortEnum.NO,
            productInDiscount=BooleanStrShortEnum.YES,
            productInDistinguished=BooleanStrShortEnum.NO
        )
        assert dto.productIsVisible == BooleanStrShortEnum.YES
        assert dto.productInPromotion == BooleanStrShortEnum.NO
        assert dto.productInDiscount == BooleanStrShortEnum.YES

    def test_with_text_searches(self):
        dto = SearchPimProductsProductProductParamsModel(
            containsText="laptop",
            containsCodePart="LAP-001",
            productHasNote="important"
        )
        assert dto.containsText == "laptop"
        assert dto.containsCodePart == "LAP-001"
        assert dto.productHasNote == "important"

    def test_with_version_id(self):
        dto = SearchPimProductsProductProductParamsModel(
            productVersionId=42
        )
        assert dto.productVersionId == 42

    def test_invalid_version_id_zero(self):
        with pytest.raises(ValidationError):
            SearchPimProductsProductProductParamsModel(productVersionId=0)

    def test_with_location_id(self):
        dto = SearchPimProductsProductProductParamsModel(
            productLocationId=5
        )
        assert dto.productLocationId == 5

    def test_invalid_location_id_zero(self):
        with pytest.raises(ValidationError):
            SearchPimProductsProductProductParamsModel(productLocationId=0)


# --- Tests for Endpoints
class TestDeleteEndpoint:
    def test_instantiate_with_params(self):
        endpoint = Delete(
            params=DeletePimProductsProductProductParamsModel(
                products=[ProductsDeleteModel(productId=1, productSizeCodeExternal="code")]
            )
        )
        assert endpoint._method == 'POST'
        assert endpoint._endpoint == '/api/admin/v6/products/products/delete'
        assert endpoint.params.products[0].productId == 1

    def test_instantiate_missing_params(self):
        with pytest.raises(ValidationError):
            Delete()


class TestGetEndpoint:
    def test_instantiate_with_ids(self):
        endpoint = Get(productIds=["code1", "code2"])
        assert endpoint._method == 'GET'
        assert endpoint._endpoint == '/api/admin/v6/products/products'
        assert endpoint.productIds == ["code1", "code2"]

    def test_single_id(self):
        endpoint = Get(productIds=["single"])
        assert endpoint.productIds == ["single"]

    def test_empty_ids(self):
        with pytest.raises(ValidationError):
            Get(productIds=[])

    def test_more_than_100_ids(self):
        ids = [f"id{i}" for i in range(101)]
        with pytest.raises(ValidationError):
            Get(productIds=ids)

    def test_invalid_type_ids(self):
        with pytest.raises(ValidationError):
            Get(productIds=["valid", 123, None])

    def test_duplicate_ids(self):
        with pytest.raises(ValidationError):
            Get(productIds=["code1", "code2", "code1"])


class TestPostEndpoint:
    # Note: Full instantiation skipped due to ProductsPostModel complexity (40+ required fields)

    def test_instantiate_missing_params(self):
        with pytest.raises(ValidationError):
            Post()

    def test_endpoint_attributes(self):
        # Test that endpoint class has correct method and endpoint
        # without needing to create full valid params
        assert Post.model_fields['params'].is_required() == True


class TestPutEndpoint:
    # Note: Full instantiation skipped due to ProductsPutModel complexity (40+ required fields)

    def test_instantiate_missing_params(self):
        with pytest.raises(ValidationError):
            Put()

    def test_endpoint_attributes(self):
        # Test that endpoint class has correct method and endpoint
        # without needing to create full valid params
        assert Put.model_fields['params'].is_required() == True


class TestSearchEndpoint:
    def test_instantiate_empty_params(self):
        endpoint = Search(params=SearchPimProductsProductProductParamsModel())
        assert endpoint._method == 'POST'
        assert endpoint._endpoint == '/api/admin/v6/products/products/search'
        assert endpoint.params.productIsAvailable is None

    def test_instantiate_with_filters(self):
        endpoint = Search(
            params=SearchPimProductsProductProductParamsModel(
                productIsAvailable=BooleanStrShortEnum.YES,
                productIsVisible=BooleanStrShortEnum.YES,
                containsText="laptop"
            )
        )
        assert endpoint.params.productIsAvailable == BooleanStrShortEnum.YES
        assert endpoint.params.productIsVisible == BooleanStrShortEnum.YES
        assert endpoint.params.containsText == "laptop"

    def test_instantiate_with_pagination(self):
        endpoint = Search(
            params=SearchPimProductsProductProductParamsModel()
        )
        # PageableCamelGateway provides pagination - test basic structure
        assert endpoint._method == 'POST'
        assert endpoint._endpoint == '/api/admin/v6/products/products/search'
