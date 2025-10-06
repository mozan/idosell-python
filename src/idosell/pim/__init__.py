# Sizes
from .sizes import Get as SizesGet
from .sizes import Put as SizesPut

# Sizecharts
from .sizecharts import Delete as SizechartsDelete
from .sizecharts import Get as SizechartsGet
from .sizecharts import Put as SizechartsPut

# Menu
from .menu import GetFilter as MenuGetFilter
from .menu import PutFilter as MenuPutFilter
from .menu import Delete as MenuDelete
from .menu import Get as MenuGet
from .menu import Post as MenuPost
from .menu import Put as MenuPut
from .menu import PutSort as MenuPutSort

# Responsibility
from .responsibility import GetEntities as ResponsibilityGetEntities
from .responsibility import PostEntities as ResponsibilityPostEntities
from .responsibility import PutEntities as ResponsibilityPutEntities
from .responsibility import DeleteEntities as ResponsibilityDeleteEntities

# Warranties
from .warranties import GetCountTotal as WarrantiesGetCountTotal
from .warranties import PutLanguageData as WarrantiesPutLanguageData
from .warranties import Delete as WarrantiesDelete
from .warranties import Get as WarrantiesGet
from .warranties import Post as WarrantiesPost
from .warranties import Put as WarrantiesPut

# Products submodule
from . import products

__all__ = [
    # Sizes
    'SizesGet', 'SizesPut',
    # Sizecharts
    'SizechartsDelete', 'SizechartsGet', 'SizechartsPut',
    # Menu
    'MenuGetFilter', 'MenuPutFilter', 'MenuDelete', 'MenuGet', 'MenuPost', 'MenuPut', 'MenuPutSort',
    # Responsibility
    'ResponsibilityGetEntities', 'ResponsibilityPostEntities', 'ResponsibilityPutEntities', 'ResponsibilityDeleteEntities',
    # Warranties
    'WarrantiesGetCountTotal', 'WarrantiesPutLanguageData', 'WarrantiesDelete', 'WarrantiesGet', 'WarrantiesPost', 'WarrantiesPut',
    # Products submodule
    'products'
]
