from typing import List
from pydantic import BaseModel, Field, PrivateAttr, StrictInt

from src.idosell._common import AppendableGateway, Gateway, PageableCamelGateway
from src.idosell.pim._common import EntityTypeEnum


# --- DTOs
class EntitiesResponsibilityModel(BaseModel):
    code: str = Field(..., description="Short name/code")
    name: str = Field(..., description="Full name")
    mail: str = Field(..., description="E-mail address")
    street: str = Field(..., description="Street")
    number: str | None = Field(None, description="Building number")
    subnumber: str | None = Field(None, description="Apartment number")
    zipcode: str = Field(..., description="Zipcode")
    city: str = Field(..., description="City")
    country: str = Field(..., description="2-letter ISO country code")
    phone: str | None = Field(None, description="Phone number")
    description: str | None = Field(None, description="Additional description")
    url: str | None = Field(None, description="URL to contact page")

class EntitiesResponsibilityPostModel(EntitiesResponsibilityModel):
    id: int | None = Field(None, ge=1, description="Identificator of the entity")

class EntitiesResponsibilityPutModel(EntitiesResponsibilityModel):
    id: StrictInt = Field(..., ge=1, description="Identificator of the entity")

class PostEntitiesPimResponsabilityParamsModel(BaseModel):
    entities: List[EntitiesResponsibilityPostModel] = Field(..., min_length=1, max_length=100, description="...")
    type: EntityTypeEnum = Field(..., description="Type of entity")

class PutEntitiesPimResponsabilityParamsModel(BaseModel):
    entities: List[EntitiesResponsibilityPutModel] = Field(..., min_length=1, max_length=100, description="...")
    type: EntityTypeEnum = Field(..., description="Type of entity")


# --- ENDPOINTS
class GetEntities(PageableCamelGateway):
    """
    This call returns a list of responsible entities.
    DOCS_URL: https://idosell.readme.io/reference/responsibilityentitiesget-1
    """

    _method: str = PrivateAttr(default='GET')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/responsibility/entities')

    code: List[str] | None = Field(None, description="List of codes")
    type: str | None = Field(None, description="Type of entity")

class PostEntities(AppendableGateway):
    """
    Use this operation to create responsible entities.
    DOCS_URL: https://idosell.readme.io/reference/responsibilityentitiespost-1
    """

    _method: str = PrivateAttr(default='POST')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/responsibility/entities')

    params: PostEntitiesPimResponsabilityParamsModel = Field(..., description="Parameters transmitted to method")

class PutEntities(AppendableGateway):
    """
    Use this operation to update responsible entities
    DOCS_URL: https://idosell.readme.io/reference/responsibilityentitiesput-1
    """

    _method: str = PrivateAttr(default='PUT')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/responsibility/entities')

    params: PutEntitiesPimResponsabilityParamsModel = Field(..., description="Parameters transmitted to method")

class DeleteEntities(Gateway):
    """
    This call is used to remove responsible entities
    DOCS_URL: https://idosell.readme.io/reference/responsibilityentitiesdelete-1
    """

    _method: str = PrivateAttr(default='DELETE')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/responsibility/entities')

    code: List[str] = Field(..., description="List of codes")
    type: str = Field(..., description="Type of entity")
