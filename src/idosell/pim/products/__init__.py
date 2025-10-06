# Parameters
from .parameters import Delete as ParametersDelete
from .parameters import Put as ParametersPut
from .parameters import Search as ParametersSearch

# Images
from .images import Delete as ImagesDelete
from .images import Put as ImagesPut

# Groups
from .groups import PutMainProduct as GroupsPutMainProduct
from .groups import PutOrder as GroupsPutOrder
from .groups import PutSettings as GroupsPutSettings

# Strikethrough
from .strikethrough import GetPrices as StrikethroughGetPrices
from .strikethrough import PutPrices as StrikethroughPutPrices

# Omnibus
from .omnibus import GetPrices as OmnibusGetPrices
from .omnibus import PutPrices as OmnibusPutPrices

# Synchronization
from .synchronization import PostFile as SynchronizationPostFile
from .synchronization import PutFinishUpload as SynchronizationPutFinishUpload

# Supplier
from .supplier import PutCode as SupplierPutCode
from .supplier import PutProductData as SupplierPutProductData

# Collections
from .collections import Post as CollectionsPost
from .collections import DeleteProducts as CollectionsDeleteProducts
from .collections import PostProducts as CollectionsPostProducts
from .collections import PutProducts as CollectionsPutProducts
from .collections import PutRenew as CollectionsPutRenew

# Miscs
from .miscs import GetProductsAuctions
from .miscs import GetProductsCodeExistence
from .miscs import GetProductsIdBySizecode
from .miscs import GetProductsReservations
from .miscs import GetProductsSKUbyBarcode
from .miscs import PostProductsRestore
from .miscs import PutProductsAttachments
from .miscs import SearchProductsDeliveryTime

# Descriptions
from .descriptions import Get as DescriptionsGet
from .descriptions import Put as DescriptionsPut

# Sizes
from .sizes import Delete as SizesDelete
from .sizes import Get as SizesGet
from .sizes import Put as SizesPut

# Opinions
from .opinions import Delete as OpinionsDelete
from .opinions import Get as OpinionsGet
from .opinions import Post as OpinionsPost
from .opinions import Put as OpinionsPut
from .opinions import GetRate as OpinionsGetRate

# Bundles
from .bundles import PostBundles as BundlesPostBundles
from .bundles import DeleteProducts as BundlesDeleteProducts
from .bundles import PostProducts as BundlesPostProducts
from .bundles import PutProductsQuantity as BundlesPutProductsQuantity
from .bundles import PutRenew as BundlesPutRenew

# Questions
from .questions import Get as QuestionsGet
from .questions import Put as QuestionsPut

# Marketing
from .marketing import GetAllFacebookCatalogIds
from .marketing import GetPromotion as MarketingGetPromotion
from .marketing import PostPromotion as MarketingPostPromotion
from .marketing import PutPromotion as MarketingPutPromotion
from .marketing import GetZones as MarketingGetZones
from .marketing import PutZones as MarketingPutZones

# Categories
from .categories import Get as CategoriesGet
from .categories import Put as CategoriesPut
from .categories import SearchIdosell as CategoriesSearchIdosell

# Brands
from .brands import Delete as BrandsDelete
from .brands import GetFilter as BrandsGetFilter
from .brands import PutFilter as BrandsPutFilter
from .brands import Get as BrandsGet
from .brands import Post as BrandsPost
from .brands import Put as BrandsPut

# Series
from .series import Delete as SeriesDelete
from .series import GetFilter as SeriesGetFilter
from .series import PutFilter as SeriesPutFilter
from .series import Get as SeriesGet
from .series import Put as SeriesPut

# Stocks
from .stocks import PutQuantity as StocksPutQuantity
from .stocks import Get as StocksGet
from .stocks import Put as StocksPut

# Product subdirectory
from .product import (
    Delete as ProductDelete,
    Get as ProductGet,
    Post as ProductPost,
    Put as ProductPut,
    Search as ProductSearch,
    DeleteToFacebookCatalog,
    GetToFacebookCatalog,
    PostToFacebookCatalog,
    DeleteProductsToPromotion,
    PostProductsToPromotion
)

__all__ = [
    # Parameters
    'ParametersDelete', 'ParametersPut', 'ParametersSearch',
    # Images
    'ImagesDelete', 'ImagesPut',
    # Groups
    'GroupsPutMainProduct', 'GroupsPutOrder', 'GroupsPutSettings',
    # Strikethrough
    'StrikethroughGetPrices', 'StrikethroughPutPrices',
    # Omnibus
    'OmnibusGetPrices', 'OmnibusPutPrices',
    # Synchronization
    'SynchronizationPostFile', 'SynchronizationPutFinishUpload',
    # Supplier
    'SupplierPutCode', 'SupplierPutProductData',
    # Collections
    'CollectionsPost', 'CollectionsDeleteProducts', 'CollectionsPostProducts',
    'CollectionsPutProducts', 'CollectionsPutRenew',
    # Miscs
    'GetProductsAuctions', 'GetProductsCodeExistence', 'GetProductsIdBySizecode',
    'GetProductsReservations', 'GetProductsSKUbyBarcode', 'PostProductsRestore',
    'PutProductsAttachments', 'SearchProductsDeliveryTime',
    # Descriptions
    'DescriptionsGet', 'DescriptionsPut',
    # Sizes
    'SizesDelete', 'SizesGet', 'SizesPut',
    # Opinions
    'OpinionsDelete', 'OpinionsGet', 'OpinionsPost', 'OpinionsPut', 'OpinionsGetRate',
    # Bundles
    'BundlesPostBundles', 'BundlesDeleteProducts', 'BundlesPostProducts',
    'BundlesPutProductsQuantity', 'BundlesPutRenew',
    # Questions
    'QuestionsGet', 'QuestionsPut',
    # Marketing
    'GetAllFacebookCatalogIds', 'MarketingGetPromotion', 'MarketingPostPromotion',
    'MarketingPutPromotion', 'MarketingGetZones', 'MarketingPutZones',
    # Categories
    'CategoriesGet', 'CategoriesPut', 'CategoriesSearchIdosell',
    # Brands
    'BrandsDelete', 'BrandsGetFilter', 'BrandsPutFilter', 'BrandsGet', 'BrandsPost', 'BrandsPut',
    # Series
    'SeriesDelete', 'SeriesGetFilter', 'SeriesPutFilter', 'SeriesGet', 'SeriesPut',
    # Stocks
    'StocksPutQuantity', 'StocksGet', 'StocksPut',
    # Product subdirectory
    'ProductDelete', 'ProductGet', 'ProductPost', 'ProductPut', 'ProductSearch',
    'DeleteToFacebookCatalog', 'GetToFacebookCatalog', 'PostToFacebookCatalog',
    'DeleteProductsToPromotion', 'PostProductsToPromotion'
]
