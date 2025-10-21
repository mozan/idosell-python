from pydantic import BaseModel, Field, PrivateAttr

from src.idosell._common import AppendableGateway, Gateway, IdoSellLanguageId, PageableCamelGateway
from src.idosell.pim._common import SizeChartsPutModel


# --- DTOs
class DeletePimSizechartsParamsModel(BaseModel):
    ids: list[int] = Field(..., description="!identyfikatory!#")

class PutPimSizechartsParamsModel(BaseModel):
    sizeCharts: list[SizeChartsPutModel] = Field(..., description="...")


# --- ENDPOINTS
class Delete(Gateway):
    """
    The method allows the removal of size charts
    DOCS_URL: https://idosell.readme.io/v6.0/reference/sizechartssizechartsdeletepost
    """

    _method: str = PrivateAttr(default='POST')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/sizecharts/sizecharts/delete')

    params: DeletePimSizechartsParamsModel = Field(..., description="Parameters transmitted to method")

class Get(PageableCamelGateway):
    """
    The method allows size charts to be downloaded.
    DOCS_URL: https://idosell.readme.io/v6.0/reference/sizechartssizechartsget
    """

    _method: str = PrivateAttr(default='GET')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/sizecharts/sizecharts')

    ids: list[int] | None = Field(None, description="IDs")
    names: list[str] | None = Field(None, description="Names of size charts")
    languages: list[IdoSellLanguageId] | None = Field(None, description="List of languages")

class Put(AppendableGateway):
    """
    The method allows the size charts settings to be updated
    DOCS_URL: https://idosell.readme.io/v6.0/reference/sizechartssizechartsput
    """

    _method: str = PrivateAttr(default='PUT')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/sizecharts/sizecharts')

    params: PutPimSizechartsParamsModel = Field(..., description="Parameters transmitted to method")
