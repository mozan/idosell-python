from pydantic import BaseModel, Field, PrivateAttr, StrictInt

from src.idosell._common import AppendableGateway
from src.idosell.pim.products._common import ProductsImages, ProductsImagesSettingsModel


# --- DTOs
class DeletePimProductsImagesParamsModel(BaseModel):
    deleteAll: bool = Field(..., description="Delete all images")
    productId: StrictInt = Field(..., ge=1, description="Product IAI code")
    shopId: StrictInt = Field(..., ge=1, description="Shop Id")
    productImagesId: list[str] = Field(..., min_length=1, description="List of product image IDs") # type: ignore

class PutPimProductsImagesParamsModel(BaseModel):
    productsImagesSettings: ProductsImagesSettingsModel = Field(..., description="Product images settings")
    productsImages: list[ProductsImages] = Field(..., min_length=1, description="Information on product images") # type: ignore


# --- ENDPOINTS
class Delete(AppendableGateway):
    """
    This method is used to delete images of products
    DOCS_URL: https://idosell.readme.io/v6.0/reference/productsimagesdeletepost
    """

    _method: str = PrivateAttr(default='POST')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/products/images/delete')

    params: list[DeletePimProductsImagesParamsModel] = Field(..., description="Parameters for deleting product images")

class Put(AppendableGateway):
    """
    Method used for adding and editing product pictures
    DOCS_URL: https://idosell.readme.io/v6.0/reference/productsimagesput
    """

    _method: str = PrivateAttr(default='PUT')
    _endpoint: str = PrivateAttr(default='/api/admin/v6/products/images')

    params: PutPimProductsImagesParamsModel = Field(..., description="Parameters for updating product images")
