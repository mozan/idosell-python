# Suppliers
from .suppliers import Delete as SuppliersDelete
from .suppliers import Get as SuppliersGet
from .suppliers import Put as SuppliersPut

# Locations
from .locations import GetLocations

# Stocks
from .stocks import PutAcceptMM as StocksPutAcceptMM
from .stocks import PutClose as StocksPutClose
from .stocks import DeleteDocuments as StocksDeleteDocuments
from .stocks import GetDocuments as StocksGetDocuments
from .stocks import PostDocuments as StocksPostDocuments
from .stocks import PutDocuments as StocksPutDocuments
from .stocks import GetOpenedDocuments as StocksGetOpenedDocuments
from .stocks import DeleteProducts as StocksDeleteProducts
from .stocks import GetProducts as StocksGetProducts
from .stocks import PostProducts as StocksPostProducts
from .stocks import PutProducts as StocksPutProducts
from .stocks import PutRejectMM as StocksPutRejectMM

__all__ = [
    # Suppliers
    'SuppliersDelete', 'SuppliersGet', 'SuppliersPut',
    # Locations
    'GetLocations',
    # Stocks
    'StocksPutAcceptMM', 'StocksPutClose', 'StocksDeleteDocuments', 'StocksGetDocuments',
    'StocksPostDocuments', 'StocksPutDocuments', 'StocksGetOpenedDocuments',
    'StocksDeleteProducts', 'StocksGetProducts', 'StocksPostProducts', 'StocksPutProducts',
    'StocksPutRejectMM'
]
