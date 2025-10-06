import pytest
from pydantic import ValidationError

from src.idosell.crm.pricelists import (
    ReturnElementsPriceListsEnum,
    ProductsModel, ProducersPriceListsModel, SeriesPriceListsModel,
    CategoriesPriceListsModel, MenuItemsPriceListsModel,
    PutClientsCrmPricelistsParamsModel, DeleteCrmPricelistsParamsModel,
    PostCrmPricelistsParamsModel, PutCrmPricelistsParamsModel,
    PutProductsCrmPricelistsParamsModel, PutRenameCrmPricelistsParamsModel,
    GetClients, PutClients, Delete, Get, Post, Put, GetProducts, PutProducts, PutRename
)
from src.idosell._common import BooleanStrLongEnum


# --- Tests for Enums
class TestReturnElementsPriceListsEnum:
    def test_valid_values(self):
        assert ReturnElementsPriceListsEnum.PRICELISTID == 'priceListId'
        assert ReturnElementsPriceListsEnum.PRICELISTNAME == 'priceListName'
        assert ReturnElementsPriceListsEnum.ONLYORDERPRODUCTSWITHMANUALLYSETPRICES == 'onlyOrderProductsWithManuallySetPrices'
        assert ReturnElementsPriceListsEnum.ONLYSEEPRODUCTSWITHMANUALLYSETPRICES == 'onlySeeProductsWithManuallySetPrices'


# --- Tests for DTOs
class TestProductsModel:
    def test_valid(self):
        dto = ProductsModel(
            productId=1,
            price=99.99,
            currencyId="USD"
        )
        assert dto.productId == 1
        assert dto.price == 99.99
        assert dto.currencyId == "USD"

    def test_invalid_productId_zero(self):
        with pytest.raises(ValidationError):
            ProductsModel(productId=0, price=10.0, currencyId="USD")

    def test_invalid_productId_negative(self):
        with pytest.raises(ValidationError):
            ProductsModel(productId=-1, price=10.0, currencyId="USD")

class TestProducersPriceListsModel:
    def test_valid(self):
        dto = ProducersPriceListsModel(
            producerId=5,
            price=199.99,
            currencyId="EUR"
        )
        assert dto.producerId == 5
        assert dto.price == 199.99

    def test_invalid_producerId_zero(self):
        with pytest.raises(ValidationError):
            ProducersPriceListsModel(producerId=0, price=10.0, currencyId="EUR")

class TestSeriesPriceListsModel:
    def test_valid(self):
        dto = SeriesPriceListsModel(
            seriesId=3,
            price=299.99,
            currencyId="GBP"
        )
        assert dto.seriesId == 3
        assert dto.price == 299.99

    def test_invalid_seriesId_zero(self):
        with pytest.raises(ValidationError):
            SeriesPriceListsModel(seriesId=0, price=10.0, currencyId="GBP")

class TestCategoriesPriceListsModel:
    def test_valid(self):
        dto = CategoriesPriceListsModel(
            categoryId=10,
            price=49.99,
            currencyId="PLN"
        )
        assert dto.categoryId == 10
        assert dto.currencyId == "PLN"

    def test_invalid_categoryId_zero(self):
        with pytest.raises(ValidationError):
            CategoriesPriceListsModel(categoryId=0, price=10.0, currencyId="PLN")

class TestMenuItemsPriceListsModel:
    def test_valid(self):
        dto = MenuItemsPriceListsModel(
            menuItemId=7,
            price=79.99,
            currencyId="USD"
        )
        assert dto.menuItemId == 7
        assert dto.price == 79.99

    def test_invalid_menuItemId_zero(self):
        with pytest.raises(ValidationError):
            MenuItemsPriceListsModel(menuItemId=0, price=10.0, currencyId="USD")

class TestPutClientsCrmPricelistsParamsModel:
    def test_valid(self):
        dto = PutClientsCrmPricelistsParamsModel(
            priceListId=1,
            clientsIds=[10, 20, 30]
        )
        assert dto.priceListId == 1
        assert dto.clientsIds == [10, 20, 30]

    def test_invalid_priceListId_zero(self):
        with pytest.raises(ValidationError):
            PutClientsCrmPricelistsParamsModel(priceListId=0, clientsIds=[1])

class TestDeleteCrmPricelistsParamsModel:
    def test_valid(self):
        dto = DeleteCrmPricelistsParamsModel(priceListId=5)
        assert dto.priceListId == 5

    def test_invalid_priceListId_zero(self):
        with pytest.raises(ValidationError):
            DeleteCrmPricelistsParamsModel(priceListId=0)

class TestPostCrmPricelistsParamsModel:
    def test_valid(self):
        dto = PostCrmPricelistsParamsModel(
            priceListName="VIP Customers",
            onlyOrderProductsWithManuallySetPrices=BooleanStrLongEnum.YES,
            onlySeeProductsWithManuallySetPrices=BooleanStrLongEnum.NO
        )
        assert dto.priceListName == "VIP Customers"
        assert dto.onlyOrderProductsWithManuallySetPrices == BooleanStrLongEnum.YES
        assert dto.onlySeeProductsWithManuallySetPrices == BooleanStrLongEnum.NO

class TestPutCrmPricelistsParamsModel:
    def test_valid(self):
        dto = PutCrmPricelistsParamsModel(
            priceListId=2,
            priceListName="Updated VIP",
            onlyOrderProductsWithManuallySetPrices=BooleanStrLongEnum.NO,
            onlySeeProductsWithManuallySetPrices=BooleanStrLongEnum.YES
        )
        assert dto.priceListId == 2
        assert dto.priceListName == "Updated VIP"

    def test_invalid_priceListId_zero(self):
        with pytest.raises(ValidationError):
            PutCrmPricelistsParamsModel(
                priceListId=0,
                priceListName="Test",
                onlyOrderProductsWithManuallySetPrices=BooleanStrLongEnum.NO,
                onlySeeProductsWithManuallySetPrices=BooleanStrLongEnum.NO
            )

class TestPutProductsCrmPricelistsParamsModel:
    def test_valid(self):
        dto = PutProductsCrmPricelistsParamsModel(
            priceListId=1,
            products=[ProductsModel(productId=1, price=10.0, currencyId="USD")],
            producers=[ProducersPriceListsModel(producerId=1, price=20.0, currencyId="USD")],
            series=[SeriesPriceListsModel(seriesId=1, price=30.0, currencyId="USD")],
            categories=[CategoriesPriceListsModel(categoryId=1, price=40.0, currencyId="USD")],
            menuItems=[MenuItemsPriceListsModel(menuItemId=1, price=50.0, currencyId="USD")]
        )
        assert dto.priceListId == 1
        assert len(dto.products) == 1
        assert len(dto.producers) == 1

    def test_invalid_priceListId_zero(self):
        with pytest.raises(ValidationError):
            PutProductsCrmPricelistsParamsModel(
                priceListId=0,
                products=[],
                producers=[],
                series=[],
                categories=[],
                menuItems=[]
            )

class TestPutRenameCrmPricelistsParamsModel:
    def test_valid(self):
        dto = PutRenameCrmPricelistsParamsModel(
            priceListName="New Name",
            priceListId=3
        )
        assert dto.priceListName == "New Name"
        assert dto.priceListId == 3

    def test_invalid_priceListId_zero(self):
        with pytest.raises(ValidationError):
            PutRenameCrmPricelistsParamsModel(priceListName="Name", priceListId=0)


# --- Tests for Endpoints
class TestGetClients:
    def test_instantiate_minimal(self):
        dto = GetClients()
        assert hasattr(dto, '_method')
        assert hasattr(dto, '_endpoint')
        assert dto.priceListId is None

    def test_instantiate_with_params(self):
        dto = GetClients(priceListId=5)
        assert dto.priceListId == 5

    def test_invalid_priceListId_zero(self):
        with pytest.raises(ValidationError):
            GetClients(priceListId=0)

class TestPutClients:
    def test_instantiate(self):
        dto = PutClients(
            params=PutClientsCrmPricelistsParamsModel(
                priceListId=1,
                clientsIds=[10, 20]
            )
        )
        assert dto.params.priceListId == 1
        assert len(dto.params.clientsIds) == 2

class TestDelete:
    def test_instantiate(self):
        dto = Delete(
            params=DeleteCrmPricelistsParamsModel(priceListId=3)
        )
        assert dto.params.priceListId == 3

class TestGet:
    def test_instantiate_minimal(self):
        dto = Get()
        assert hasattr(dto, '_method')
        assert hasattr(dto, '_endpoint')
        assert dto.priceListIds is None
        assert dto.returnElements is None

    def test_instantiate_with_params(self):
        dto = Get(
            priceListIds=[1, 2, 3],
            returnElements=[
                ReturnElementsPriceListsEnum.PRICELISTID,
                ReturnElementsPriceListsEnum.PRICELISTNAME
            ]
        )
        assert dto.priceListIds == [1, 2, 3]
        assert len(dto.returnElements) == 2

    def test_invalid_priceListIds_empty(self):
        with pytest.raises(ValidationError):
            Get(priceListIds=[])

    def test_invalid_returnElements_empty(self):
        with pytest.raises(ValidationError):
            Get(returnElements=[])

class TestPost:
    def test_instantiate(self):
        dto = Post(
            params=PostCrmPricelistsParamsModel(
                priceListName="Test List",
                onlyOrderProductsWithManuallySetPrices=BooleanStrLongEnum.YES,
                onlySeeProductsWithManuallySetPrices=BooleanStrLongEnum.NO
            )
        )
        assert dto.params.priceListName == "Test List"

class TestPut:
    def test_instantiate(self):
        dto = Put(
            params=PutCrmPricelistsParamsModel(
                priceListId=1,
                priceListName="Updated",
                onlyOrderProductsWithManuallySetPrices=BooleanStrLongEnum.NO,
                onlySeeProductsWithManuallySetPrices=BooleanStrLongEnum.YES
            )
        )
        assert dto.params.priceListId == 1
        assert dto.params.priceListName == "Updated"

class TestGetProducts:
    def test_instantiate_minimal(self):
        dto = GetProducts()
        assert hasattr(dto, '_method')
        assert hasattr(dto, '_endpoint')
        assert dto.priceListId is None

    def test_instantiate_with_params(self):
        dto = GetProducts(priceListId=7)
        assert dto.priceListId == 7

    def test_invalid_priceListId_zero(self):
        with pytest.raises(ValidationError):
            GetProducts(priceListId=0)

class TestPutProducts:
    def test_instantiate(self):
        dto = PutProducts(
            params=PutProductsCrmPricelistsParamsModel(
                priceListId=1,
                products=[ProductsModel(productId=1, price=10.0, currencyId="USD")],
                producers=[],
                series=[],
                categories=[],
                menuItems=[]
            )
        )
        assert dto.params.priceListId == 1
        assert len(dto.params.products) == 1

class TestPutRename:
    def test_instantiate(self):
        dto = PutRename(
            params=PutRenameCrmPricelistsParamsModel(
                priceListName="Renamed List",
                priceListId=5
            )
        )
        assert dto.params.priceListName == "Renamed List"
        assert dto.params.priceListId == 5
