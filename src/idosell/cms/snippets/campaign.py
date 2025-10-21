from typing import Annotated
from pydantic import BaseModel, Field, PrivateAttr, StrictInt

from src.idosell._common import AppendableGateway, BooleanStrShortEnum, Gateway, PageableCamelGateway


# --- DTOs
class SnippetsCampaignConfigVariablesModel(BaseModel):
    key: str = Field(..., min_length=1, max_length=255, description="Key of config value")
    value: str = Field(..., max_length=255, description="Value of config item")

class SnippetsCampaignModel(BaseModel):
    description: str | None  = Field(None, description="Snippet campaign internal description")
    shop: list[int] | None  = Field(None, description="Shop ids where code snippets are active")
    active: BooleanStrShortEnum | None  = Field(None, description="Whether the snippet is active")
    order: StrictInt | None  = Field(None, description="Snippet order")
    configVariables: list[SnippetsCampaignConfigVariablesModel] | None  = Field(None, description="...")

class PostSnippetsCampaignModel(SnippetsCampaignModel):
    id: int | None = Field(None, ge=1, description="Snippet campaign id")
    name: str = Field(..., description="Snippet campaign name")

class PutSnippetsCampaignModel(SnippetsCampaignModel):
    id: StrictInt = Field(..., ge=1, description="Snippet campaign id")
    name: str | None = Field(None, description="Snippet campaign name")

class PostCmsSnippetsCampaignParamsModel(BaseModel):
    campaigns: list[PostSnippetsCampaignModel] = Field(..., min_length=1, max_length=100, description="...") # type: ignore

class PutCmsSnippetsCampaignParamsModel(BaseModel):
    campaigns: list[PutSnippetsCampaignModel] = Field(..., min_length=1, max_length=100, description="...") # type: ignore


# --- ENDPOINTS
class Get(PageableCamelGateway):
    """
    This call returns all snippet campaigns (including deleted ones but to readonly)
    DOCS_URL: https://idosell.readme.io/reference/snippetscampaignget-1
    """

    _method: str = PrivateAttr(default='GET')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/snippets/campaign')

    shopId: list[Annotated[int, Field(ge=1)]] | None = Field(default=None, min_length=1, description="List of shop identifiers") # type: ignore
    id: list[Annotated[int, Field(ge=1)]] | None = Field(default=None, min_length=1, description="List of identifiers") # type: ignore
    omitDeleted: BooleanStrShortEnum | None = Field(default=None, description="Whether to skip the return of deleted campaigns")

class Post(AppendableGateway):
    """
    Use this operation to create snippet campaigns
    DOCS_URL: https://idosell.readme.io/reference/snippetscampaignpost-1
    """

    _method: str = PrivateAttr(default='POST')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/snippets/campaign')

    params: PostCmsSnippetsCampaignParamsModel = Field(..., description="...")

class Put(AppendableGateway):
    """
    Use this operation to update snippet campaigns
    DOCS_URL: https://idosell.readme.io/reference/snippetscampaignput-1
    """

    _method: str = PrivateAttr(default='PUT')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/snippets/campaign')

    params: PutCmsSnippetsCampaignParamsModel = Field(..., description="...")

class Delete(Gateway):
    """
    This call is used to remove campaign snippets
    DOCS_URL: https://idosell.readme.io/reference/snippetscampaigndelete-1
    """

    _method: str = PrivateAttr(default='DELETE')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/snippets/campaign')

    id: list[int] = Field(..., min_length=1, max_length=100, description="List of identifiers") # type: ignore
