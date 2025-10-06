# Subscriptions
from .subscriptions import PostAddProduct as SubscriptionsPostAddProduct
from .subscriptions import PostChangeDeliveryDates as SubscriptionsPostChangeDeliveryDates
from .subscriptions import PostChangePriceAutoUpdate as SubscriptionsPostChangePriceAutoUpdate
from .subscriptions import PostChangeStatus as SubscriptionsPostChangeStatus
from .subscriptions import DeleteProduct as SubscriptionsDeleteProduct
from .subscriptions import PostEdit as SubscriptionsPostEdit
from .subscriptions import PostEditProduct as SubscriptionsPostEditProduct
from .subscriptions import PostItemsList as SubscriptionsPostItemsList
from .subscriptions import PostListViewFetchIds as SubscriptionsPostListViewFetchIds
from .subscriptions import PostListViewList as SubscriptionsPostListViewList
from .subscriptions import PostSetRebateCode as SubscriptionsPostSetRebateCode
from .subscriptions import PostUnsetRebateCode as SubscriptionsPostUnsetRebateCode

# Refunds
from .refunds import PostAddAutomatic as RefundsPostAddAutomatic
from .refunds import PostAddAutomaticForOrder as RefundsPostAddAutomaticForOrder
from .refunds import PostAddManual as RefundsPostAddManual
from .refunds import PutCancelRefund as RefundsPutCancelRefund
from .refunds import PutConfirm as RefundsPutConfirm
from .refunds import GetPossibleAuto as RefundsGetPossibleAuto
from .refunds import GetStatus as RefundsGetStatus
from .refunds import GetRetrieveList as RefundsGetRetrieveList
from .refunds import PutUpdate as RefundsPutUpdate

# Payments
from .payments import PostCancel as PaymentsPostCancel
from .payments import PostCashback as PaymentsPostCashback
from .payments import PutConfirm as PaymentsPutConfirm
from .payments import GetForms as PaymentsGetForms
from .payments import Get as PaymentsGet
from .payments import Post as PaymentsPost
from .payments import Put as PaymentsPut
from .payments import GetProfiles as PaymentsGetProfiles
from .payments import PostRepayment as PaymentsPostRepayment

# Packages
from .packages import GetLabels as PackagesGetLabels
from .packages import PostLabels as PackagesPostLabels
from .packages import Post as PackagesPost
from .packages import Put as PackagesPut
from .packages import Search as PackagesSearch

# RMA
from .rma import Get as RmaGet
from .rma import Put as RmaPut
from .rma import GetStatuses as RmaGetStatuses

# Returns
from .returns import Get as ReturnsGet
from .returns import Post as ReturnsPost
from .returns import Put as ReturnsPut
from .returns import PutSerialNumber as ReturnsPutSerialNumber
from .returns import GetStatuses as ReturnsGetStatuses

# Orders
from .orders import GetAnalytics as OrdersGetAnalytics
from .orders import GetAuctionDetails as OrdersGetAuctionDetails
from .orders import PutClient as OrdersPutClient
from .orders import PutCourier as OrdersPutCourier
from .orders import PutDeliveryAddress as OrdersPutDeliveryAddress
from .orders import PutDevide as OrdersPutDevide
from .orders import PostDocumentsCreate as OrdersPostDocumentsCreate
from .orders import DeleteDocuments as OrdersDeleteDocuments
from .orders import GetDocuments as OrdersGetDocuments
from .orders import PostDocuments as OrdersPostDocuments
from .orders import GetExportdocumentsEPP as OrdersGetExportdocumentsEPP
from .orders import GetExportdocumentsJPK as OrdersGetExportdocumentsJPK
from .orders import GetHandler as OrdersGetHandler
from .orders import PutHandler as OrdersPutHandler
from .orders import GetHistory as OrdersGetHistory
from .orders import DeleteImages as OrdersDeleteImages
from .orders import GetImages as OrdersGetImages
from .orders import PostImages as OrdersPostImages
from .orders import GetLabels as OrdersGetLabels
from .orders import SearchOpinions as OrdersSearchOpinions
from .orders import GetOpinionsRate as OrdersGetOpinionsRate
from .orders import Get as OrdersGet
from .orders import Post as OrdersPost
from .orders import Put as OrdersPut
from .orders import Search as OrdersSearch
from .orders import GetPackages as OrdersGetPackages
from .orders import PostPackages as OrdersPostPackages
from .orders import PutPackages as OrdersPutPackages
from .orders import PutPickupPoint as OrdersPutPickupPoint
from .orders import GetPrinterDocuments as OrdersGetPrinterDocuments
from .orders import PutProductsSerialNumbers as OrdersPutProductsSerialNumbers
from .orders import PutProfitMargin as OrdersPutProfitMargin
from .orders import GetProfitability as OrdersGetProfitability
from .orders import PutShippingCosts as OrdersPutShippingCosts
from .orders import SearchUnfinished as OrdersSearchUnfinished
from .orders import GetWarehouse as OrdersGetWarehouse
from .orders import PutWarehouse as OrdersPutWarehouse

__all__ = [
    # Subscriptions
    'SubscriptionsPostAddProduct', 'SubscriptionsPostChangeDeliveryDates',
    'SubscriptionsPostChangePriceAutoUpdate', 'SubscriptionsPostChangeStatus',
    'SubscriptionsDeleteProduct', 'SubscriptionsPostEdit', 'SubscriptionsPostEditProduct',
    'SubscriptionsPostItemsList', 'SubscriptionsPostListViewFetchIds', 'SubscriptionsPostListViewList',
    'SubscriptionsPostSetRebateCode', 'SubscriptionsPostUnsetRebateCode',
    # Refunds
    'RefundsPostAddAutomatic', 'RefundsPostAddAutomaticForOrder', 'RefundsPostAddManual',
    'RefundsPutCancelRefund', 'RefundsPutConfirm', 'RefundsGetPossibleAuto', 'RefundsGetStatus',
    'RefundsGetRetrieveList', 'RefundsPutUpdate',
    # Payments
    'PaymentsPostCancel', 'PaymentsPostCashback', 'PaymentsPutConfirm', 'PaymentsGetForms',
    'PaymentsGet', 'PaymentsPost', 'PaymentsPut', 'PaymentsGetProfiles', 'PaymentsPostRepayment',
    # Packages
    'PackagesGetLabels', 'PackagesPostLabels', 'PackagesPost', 'PackagesPut', 'PackagesSearch',
    # RMA
    'RmaGet', 'RmaPut', 'RmaGetStatuses',
    # Returns
    'ReturnsGet', 'ReturnsPost', 'ReturnsPut', 'ReturnsPutSerialNumber', 'ReturnsGetStatuses',
    # Orders
    'OrdersGetAnalytics', 'OrdersGetAuctionDetails', 'OrdersPutClient', 'OrdersPutCourier',
    'OrdersPutDeliveryAddress', 'OrdersPutDevide', 'OrdersPostDocumentsCreate', 'OrdersDeleteDocuments',
    'OrdersGetDocuments', 'OrdersPostDocuments', 'OrdersGetExportdocumentsEPP', 'OrdersGetExportdocumentsJPK',
    'OrdersGetHandler', 'OrdersPutHandler', 'OrdersGetHistory', 'OrdersDeleteImages', 'OrdersGetImages',
    'OrdersPostImages', 'OrdersGetLabels', 'OrdersSearchOpinions', 'OrdersGetOpinionsRate',
    'OrdersGet', 'OrdersPost', 'OrdersPut', 'OrdersSearch', 'OrdersGetPackages', 'OrdersPostPackages',
    'OrdersPutPackages', 'OrdersPutPickupPoint', 'OrdersGetPrinterDocuments',
    'OrdersPutProductsSerialNumbers', 'OrdersPutProfitMargin', 'OrdersGetProfitability',
    'OrdersPutShippingCosts', 'OrdersSearchUnfinished', 'OrdersGetWarehouse', 'OrdersPutWarehouse'
]
