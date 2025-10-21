from pydantic import BaseModel, Field, PrivateAttr, StrictInt

from src.idosell._common import AppendableGateway, BooleanStrShortEnum, Gateway, PageableCamelGateway
from src.idosell.pim.products._common import FilterActiveModel, ProducerPostModel, ProducerPutModel


# DTOs
class DeletePimProductsBrandsParamsModel(BaseModel):
    ids: list[int] = Field(..., description="!IdentyfikatoryProducentow!#")

class PostPimProductsBrandsParamsModel(BaseModel):
    producers: list[ProducerPostModel] = Field(..., description="List of manufacturers assigned to sought products")

class PutPimProductsBrandsParamsModel(BaseModel):
    producers: list[ProducerPutModel] = Field(..., description="List of manufacturers assigned to sought products")

class PutFilterPimProductsBrandsParamsModel(BaseModel):
    shopId: StrictInt = Field(..., ge=1, description="Shop Id")
    languageId: str = Field(..., description="Language ID (code in ISO-639-2)")
    producerId: StrictInt = Field(..., ge=1, description="Brand ID")
    filterForNodeIsDefault: BooleanStrShortEnum = Field(..., description="...")
    filtersActive: list[FilterActiveModel] = Field(..., description="Active filters")


# --- ENDPOINTS
class Delete(Gateway):
    """
    The method allows you to remove brands from the administration panel
    DOCS_URL: https://idosell.readme.io/reference/productsbrandsdeletepost
    """

    _method: str = PrivateAttr(default='POST')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/products/brands/delete')

    params: DeletePimProductsBrandsParamsModel = Field(..., description="Parameters transmitted to method")

class GetFilter(Gateway):
    """
    The method allows you to download a list of filters for brands (manufacturers) available in the IdoSell administration panel
    DOCS_URL: https://idosell.readme.io/reference/productsbrandsfilterget
    """

    _method: str = PrivateAttr(default='GET')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/products/brands/filter')

    shopId: StrictInt = Field(..., ge=1, description="Shop Id")
    languageId: str = Field(..., description="Language ID (code in ISO-639-2)")
    producerId: StrictInt = Field(..., ge=1, description="Brand ID")

class PutFilter(AppendableGateway):
    """
    The method allows you to manage filter settings for brands (manufacturers)
    DOCS_URL: https://idosell.readme.io/reference/productsbrandsfilterput
    """

    _method: str = PrivateAttr(default='PUT')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/products/brands/filter')

    params: PutFilterPimProductsBrandsParamsModel = Field(..., description="Parameters transmitted to method")

class Get(PageableCamelGateway):
    """
    Method that returns information about brands available in the IdoSell Shop administration panel
    DOCS_URL: https://idosell.readme.io/reference/productsbrandsget
    """

    _method: str = PrivateAttr(default='GET')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/products/brands')

    languagesIds: list[str] | None = Field(None, description="List of languages")

class Post(AppendableGateway):
    """
    The method allows you to update brands information available in the administration panel
    DOCS_URL: https://idosell.readme.io/reference/productsbrandspost
    """

    _method: str = PrivateAttr(default='POST')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/products/brands')

    params: PostPimProductsBrandsParamsModel = Field(..., description="Parameters transmitted to method")

class Put(AppendableGateway):
    """
    The method allows you to update brands information available in the administration panel
    DOCS_URL: https://idosell.readme.io/reference/productsbrandsput
    """

    _method: str = PrivateAttr(default='PUT')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/products/brands')

    params: PutPimProductsBrandsParamsModel = Field(..., description="Parameters transmitted to method")
