from pydantic import BaseModel, Field, PrivateAttr

from src.idosell._common import AppendableGateway, IdoSellDateTime, IdoSellLanguageId, PageableCamelGateway
from src.idosell.pim.products._common import CategoriesModel


# --- DTOs
class PutPimProductsCategoriesParamsModel(BaseModel):
    categories: list[CategoriesModel] = Field(..., description="List of categories in which sought products are present")

class SearchIdosellPimProductsCategoriesParamsModel(BaseModel):
    languagesIds: list[str] | None = Field(None, description="List of languages")
    categoriesIdoSellIds: list[str] | None = Field(None, description="Number of IdoSell Categories identifiers")
    categoriesIdoSellNames: list[str] | None = Field(None, description="IdoSell Categories name list")
    categoriesIdoSellPaths: list[str] | None = Field(None, description="IdoSell Categories path list")


# --- ENDPOINTS
class Get(PageableCamelGateway):
    """
    Method that returns information about categories configured in the administration panel
    DOCS_URL: https://idosell.readme.io/reference/productscategoriesget
    """

    _method: str = PrivateAttr(default='GET')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/products/categories')

    ids: list[int] | None = Field(None, description="List of product category identifiers in the panel")
    languages: list[IdoSellLanguageId] | None = Field(None, description="Array of languages categories names should be returned in. 'Defaults' value returns categories names in store default language. Not using languages parameter causes a situation, that categories names are returned in all available languages")
    return_last_changed_time: IdoSellDateTime | None = Field(None, description="Returns the date of last modification (YYYY-MM-DD HH:MM:SS)")

class Put(AppendableGateway):
    """
    Method that enables adding new categories to the administration panel as well editing and deleting of existing categories.
    DOCS_URL: https://idosell.readme.io/reference/productscategoriesput
    """

    _method: str = PrivateAttr(default='PUT')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/products/categories')

    params: PutPimProductsCategoriesParamsModel = Field(..., description="Parameters transmitted to method")

class SearchIdosell(PageableCamelGateway):
    """
    Method returns information about IdoSell Categories available in store
    DOCS_URL: https://idosell.readme.io/reference/productscategoriesidosellsearchpost
    """

    _method: str = PrivateAttr(default='POST')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/products/categoriesIdosell/search')

    params: SearchIdosellPimProductsCategoriesParamsModel = Field(..., description="Parameters transmitted to method")
