import pytest
from pydantic import ValidationError

from src.idosell.crm.payeraddress import (
    PayerModel, PostPayersModel, PutPayersModel,
    DeleteParamsPayersAddressModel, PostParamsPayersAddressModel, PutParamsPayersAddressModel,
    Delete, Get, Post, Put
)


# --- Tests for DTOs
class TestPayerModel:
    def test_valid(self):
        dto = PayerModel(
            clientId=100,
            payerAddressId=50
        )
        assert dto.clientId == 100
        assert dto.payerAddressId == 50

    def test_invalid_clientId_zero(self):
        with pytest.raises(ValidationError):
            PayerModel(clientId=0, payerAddressId=1)

    def test_invalid_clientId_negative(self):
        with pytest.raises(ValidationError):
            PayerModel(clientId=-1, payerAddressId=1)

    def test_invalid_payerAddressId_zero(self):
        with pytest.raises(ValidationError):
            PayerModel(clientId=1, payerAddressId=0)

class TestPostPayersModel:
    def test_valid(self):
        dto = PostPayersModel(
            clientId=200,
            payerAddressFirstName="John",
            payerAddressLastName="Doe",
            payerAddressFirm="ACME Corp",
            payerAddressNip="1234567890",
            payerAddressStreet="Main St 123",
            payerAddressZipCode="12345",
            payerAddressCity="New York",
            payerAddressCountryId="US",
            payerAddressPhone="+1234567890"
        )
        assert dto.clientId == 200
        assert dto.payerAddressFirstName == "John"
        assert dto.payerAddressLastName == "Doe"

    def test_invalid_clientId_zero(self):
        with pytest.raises(ValidationError):
            PostPayersModel(
                clientId=0,
                payerAddressFirstName="John",
                payerAddressLastName="Doe",
                payerAddressFirm="ACME",
                payerAddressNip="123",
                payerAddressStreet="St",
                payerAddressZipCode="12345",
                payerAddressCity="City",
                payerAddressCountryId="US",
                payerAddressPhone="123"
            )

class TestPutPayersModel:
    def test_valid(self):
        dto = PutPayersModel(
            clientId="300",
            payerAddressId="25",
            payerAddressFirstName="Jane",
            payerAddressLastName="Smith",
            payerAddressFirm="Tech Inc",
            payerAddressNip="0987654321",
            payerAddressStreet="Tech Ave 456",
            payerAddressZipCode="54321",
            payerAddressCity="Los Angeles",
            payerAddressCountryId="US",
            payerAddressPhone="+9876543210"
        )
        assert dto.clientId == "300"
        assert dto.payerAddressId == "25"
        assert dto.payerAddressFirstName == "Jane"

class TestDeleteParamsPayersAddressModel:
    def test_valid(self):
        dto = DeleteParamsPayersAddressModel(
            payers=[
                PayerModel(clientId=1, payerAddressId=10),
                PayerModel(clientId=2, payerAddressId=20)
            ]
        )
        assert len(dto.payers) == 2
        assert dto.payers[0].clientId == 1
        assert dto.payers[1].payerAddressId == 20

    def test_valid_single_payer(self):
        dto = DeleteParamsPayersAddressModel(
            payers=[PayerModel(clientId=5, payerAddressId=15)]
        )
        assert len(dto.payers) == 1

class TestPostParamsPayersAddressModel:
    def test_valid(self):
        dto = PostParamsPayersAddressModel(
            payers=[
                PostPayersModel(
                    clientId=100,
                    payerAddressFirstName="Alice",
                    payerAddressLastName="Johnson",
                    payerAddressFirm="Startup LLC",
                    payerAddressNip="1111111111",
                    payerAddressStreet="Innovation Blvd 789",
                    payerAddressZipCode="67890",
                    payerAddressCity="San Francisco",
                    payerAddressCountryId="US",
                    payerAddressPhone="+1111111111"
                )
            ]
        )
        assert len(dto.payers) == 1
        assert dto.payers[0].clientId == 100
        assert dto.payers[0].payerAddressFirstName == "Alice"

class TestPutParamsPayersAddressModel:
    def test_valid(self):
        dto = PutParamsPayersAddressModel(
            payers=[
                PutPayersModel(
                    clientId="200",
                    payerAddressId="30",
                    payerAddressFirstName="Bob",
                    payerAddressLastName="Williams",
                    payerAddressFirm="Enterprise Co",
                    payerAddressNip="2222222222",
                    payerAddressStreet="Business Park 321",
                    payerAddressZipCode="11111",
                    payerAddressCity="Chicago",
                    payerAddressCountryId="US",
                    payerAddressPhone="+2222222222"
                )
            ]
        )
        assert len(dto.payers) == 1
        assert dto.payers[0].clientId == "200"
        assert dto.payers[0].payerAddressId == "30"


# --- Tests for Endpoints
class TestDelete:
    def test_instantiate(self):
        dto = Delete(
            params=DeleteParamsPayersAddressModel(
                payers=[
                    PayerModel(clientId=1, payerAddressId=10)
                ]
            )
        )
        assert hasattr(dto, '_method')
        assert hasattr(dto, '_endpoint')
        assert len(dto.params.payers) == 1

    def test_instantiate_multiple_payers(self):
        dto = Delete(
            params=DeleteParamsPayersAddressModel(
                payers=[
                    PayerModel(clientId=1, payerAddressId=10),
                    PayerModel(clientId=2, payerAddressId=20),
                    PayerModel(clientId=3, payerAddressId=30)
                ]
            )
        )
        assert len(dto.params.payers) == 3

class TestGet:
    def test_instantiate_minimal(self):
        dto = Get()
        assert hasattr(dto, '_method')
        assert hasattr(dto, '_endpoint')
        assert dto.clientId is None

    def test_instantiate_with_params(self):
        dto = Get(clientId="12345")
        assert dto.clientId == "12345"

    def test_invalid_clientId_empty(self):
        with pytest.raises(ValidationError):
            Get(clientId="")

class TestPost:
    def test_instantiate(self):
        dto = Post(
            params=PostParamsPayersAddressModel(
                payers=[
                    PostPayersModel(
                        clientId=100,
                        payerAddressFirstName="Test",
                        payerAddressLastName="User",
                        payerAddressFirm="Test Corp",
                        payerAddressNip="1234567890",
                        payerAddressStreet="Test St 1",
                        payerAddressZipCode="12345",
                        payerAddressCity="Test City",
                        payerAddressCountryId="US",
                        payerAddressPhone="+1234567890"
                    )
                ]
            )
        )
        assert hasattr(dto, '_method')
        assert hasattr(dto, '_endpoint')
        assert len(dto.params.payers) == 1
        assert dto.params.payers[0].clientId == 100

class TestPut:
    def test_instantiate(self):
        dto = Put(
            params=PutParamsPayersAddressModel(
                payers=[
                    PutPayersModel(
                        clientId="200",
                        payerAddressId="50",
                        payerAddressFirstName="Updated",
                        payerAddressLastName="User",
                        payerAddressFirm="Updated Corp",
                        payerAddressNip="0987654321",
                        payerAddressStreet="Updated St 2",
                        payerAddressZipCode="54321",
                        payerAddressCity="Updated City",
                        payerAddressCountryId="PL",
                        payerAddressPhone="+9876543210"
                    )
                ]
            )
        )
        assert hasattr(dto, '_method')
        assert hasattr(dto, '_endpoint')
        assert len(dto.params.payers) == 1
        assert dto.params.payers[0].clientId == "200"
        assert dto.params.payers[0].payerAddressCity == "Updated City"
