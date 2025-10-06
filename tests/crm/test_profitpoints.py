import pytest
from pydantic import ValidationError

from src.idosell.crm.profitpoints import (
    OperationEnum,
    ClientLastPurchaseDateProfitPointsModel, PointsModificationDateModel,
    PostCrmProfitpointsParamsModel,
    Get, Post
)
from src.idosell._common import BooleanStrLongEnum
from src.idosell.crm._common import TradeCreditEnum


# --- Tests for Enums
class TestOperationEnum:
    def test_valid_values(self):
        assert OperationEnum.ADD == 'add'
        assert OperationEnum.REMOVE == 'remove'


# --- Tests for DTOs
class TestClientLastPurchaseDateProfitPointsModel:
    def test_valid(self):
        dto = ClientLastPurchaseDateProfitPointsModel(
            clientLastPurchaseDateBegin="2023-01-01",
            clientLastPurchaseDateEnd="2023-12-31"
        )
        assert dto.clientLastPurchaseDateBegin == "2023-01-01"
        assert dto.clientLastPurchaseDateEnd == "2023-12-31"

class TestPointsModificationDateModel:
    def test_valid(self):
        dto = PointsModificationDateModel(
            dateBegin="2023-01-01 00:00:00",
            dateEnd="2023-12-31 23:59:59"
        )
        assert dto.dateBegin == "2023-01-01 00:00:00"
        assert dto.dateEnd == "2023-12-31 23:59:59"

class TestPostCrmProfitpointsParamsModel:
    def test_valid_add_operation(self):
        dto = PostCrmProfitpointsParamsModel(
            client_id=100,
            operation=OperationEnum.ADD,
            score=50.5,
            note="Bonus points",
            order_number=12345
        )
        assert dto.client_id == 100
        assert dto.operation == OperationEnum.ADD
        assert dto.score == 50.5
        assert dto.note == "Bonus points"
        assert dto.order_number == 12345

    def test_valid_remove_operation(self):
        dto = PostCrmProfitpointsParamsModel(
            client_id=200,
            operation=OperationEnum.REMOVE,
            score=25.0,
            note="Used points",
            order_number=54321
        )
        assert dto.operation == OperationEnum.REMOVE

    def test_invalid_client_id_zero(self):
        with pytest.raises(ValidationError):
            PostCrmProfitpointsParamsModel(
                client_id=0,
                operation=OperationEnum.ADD,
                score=10.0,
                note="Test",
                order_number=1
            )

    def test_invalid_order_number_zero(self):
        with pytest.raises(ValidationError):
            PostCrmProfitpointsParamsModel(
                client_id=1,
                operation=OperationEnum.ADD,
                score=10.0,
                note="Test",
                order_number=0
            )


# --- Tests for Endpoints
class TestGet:
    def test_instantiate_minimal(self):
        dto = Get()
        assert hasattr(dto, '_method')
        assert hasattr(dto, '_endpoint')
        assert dto.clientsIds is None
        assert dto.clientTextSearch is None

    def test_instantiate_with_client_ids(self):
        dto = Get(clientsIds=[1, 2, 3])
        assert dto.clientsIds == [1, 2, 3]

    def test_instantiate_with_text_search(self):
        dto = Get(clientTextSearch="john.doe@example.com")
        assert dto.clientTextSearch == "john.doe@example.com"

    def test_instantiate_with_is_active(self):
        dto = Get(clientIsActive=BooleanStrLongEnum.YES)
        assert dto.clientIsActive == BooleanStrLongEnum.YES

    def test_instantiate_with_trade_credit(self):
        dto = Get(clientHasTradeCredit=TradeCreditEnum.POSITIVE)
        assert dto.clientHasTradeCredit == TradeCreditEnum.POSITIVE

    def test_instantiate_with_purchase_date(self):
        dto = Get(
            clientLastPurchaseDate=ClientLastPurchaseDateProfitPointsModel(
                clientLastPurchaseDateBegin="2023-01-01",
                clientLastPurchaseDateEnd="2023-12-31"
            )
        )
        assert dto.clientLastPurchaseDate.clientLastPurchaseDateBegin == "2023-01-01"

    def test_instantiate_with_modification_date(self):
        dto = Get(
            pointsModificationDate=PointsModificationDateModel(
                dateBegin="2023-01-01 00:00:00",
                dateEnd="2023-12-31 23:59:59"
            )
        )
        assert dto.pointsModificationDate.dateBegin == "2023-01-01 00:00:00"

    def test_instantiate_with_return_elements(self):
        dto = Get(returnElements=["clientId", "clientProfitPoints"])
        assert len(dto.returnElements) == 2

    def test_invalid_clientsIds_empty(self):
        with pytest.raises(ValidationError):
            Get(clientsIds=[])

    def test_invalid_clientTextSearch_empty(self):
        with pytest.raises(ValidationError):
            Get(clientTextSearch="")

    def test_invalid_returnElements_empty(self):
        with pytest.raises(ValidationError):
            Get(returnElements=[])

class TestPost:
    def test_instantiate(self):
        dto = Post(
            params=PostCrmProfitpointsParamsModel(
                client_id=150,
                operation=OperationEnum.ADD,
                score=100.0,
                note="Welcome bonus",
                order_number=99999
            )
        )
        assert hasattr(dto, '_method')
        assert hasattr(dto, '_endpoint')
        assert dto.params.client_id == 150
        assert dto.params.operation == OperationEnum.ADD
        assert dto.params.score == 100.0
