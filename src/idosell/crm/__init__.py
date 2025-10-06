# Externalcode
from .externalcode import Put as ExternalcodePut

# Membership
from .membership import GetCards as MembershipGetCards
from .membership import PutCards as MembershipPutCards

# Deliveryaddress
from .deliveryaddress import Delete as DeliveryaddressDelete
from .deliveryaddress import Get as DeliveryaddressGet
from .deliveryaddress import Post as DeliveryaddressPost
from .deliveryaddress import Put as DeliveryaddressPut

# Profitpoints
from .profitpoints import Get as ProfitpointsGet
from .profitpoints import Post as ProfitpointsPost

# Pricelists
from .pricelists import GetClients as PricelistsGetClients
from .pricelists import PutClients as PricelistsPutClients
from .pricelists import Delete as PricelistsDelete
from .pricelists import Get as PricelistsGet
from .pricelists import Post as PricelistsPost
from .pricelists import Put as PricelistsPut
from .pricelists import GetProducts as PricelistsGetProducts
from .pricelists import PutProducts as PricelistsPutProducts
from .pricelists import PutRename as PricelistsPutRename

# Giftcards
from .giftcards import PutBlock as GiftcardsPutBlock
from .giftcards import Delete as GiftcardsDelete
from .giftcards import Post as GiftcardsPost
from .giftcards import Put as GiftcardsPut
from .giftcards import Search as GiftcardsSearch
from .giftcards import GetTypes as GiftcardsGetTypes
from .giftcards import PutUnblock as GiftcardsPutUnblock

# Vouchers
from .vouchers import PutBlock as VouchersPutBlock
from .vouchers import GetTypes as VouchersGetTypes
from .vouchers import PutUnblock as VouchersPutUnblock
from .vouchers import Delete as VouchersDelete
from .vouchers import Get as VouchersGet
from .vouchers import Post as VouchersPost
from .vouchers import Put as VouchersPut

# Tags
from .tags import DeleteClear as TagsDeleteClear
from .tags import Delete as TagsDelete
from .tags import Get as TagsGet
from .tags import Post as TagsPost
from .tags import Put as TagsPut

# Payeraddress
from .payeraddress import Delete as PayeraddressDelete
from .payeraddress import Get as PayeraddressGet
from .payeraddress import Post as PayeraddressPost
from .payeraddress import Put as PayeraddressPut

# Discounts
from .discounts import GetGroupsClients as DiscountsGetGroupsClients
from .discounts import DeleteGroups as DiscountsDeleteGroups
from .discounts import GetGroups as DiscountsGetGroups
from .discounts import PostGroups as DiscountsPostGroups
from .discounts import PutGroups as DiscountsPutGroups
from .discounts import DeleteGroupsProducts as DiscountsDeleteGroupsProducts
from .discounts import PutGroupsProducts as DiscountsPutGroupsProducts
from .discounts import PutRebatesBlockCard as DiscountsPutRebatesBlockCard
from .discounts import DeleteRebatesCard as DiscountsDeleteRebatesCard
from .discounts import PostRebatesCard as DiscountsPostRebatesCard
from .discounts import DeleteRebatesCode as DiscountsDeleteRebatesCode
from .discounts import PostRebatesCode as DiscountsPostRebatesCode
from .discounts import PutRebatesUnblockCard as DiscountsPutRebatesUnblockCard

# Newsletter
from .newsletter import SearchEmail as NewsletterSearchEmail
from .newsletter import SearchSms as NewsletterSearchSms

# Clients
from .clients import GetBalance as ClientsGetBalance
from .clients import PostBalance as ClientsPostBalance
from .clients import Get as ClientsGet
from .clients import Post as ClientsPost
from .clients import Put as ClientsPut

# CRM
from .crm import Search as CrmSearch

# Provincelist
from .provincelist import Get as ProvincelistGet

__all__ = [
    # Externalcode
    'ExternalcodePut',
    # Membership
    'MembershipGetCards', 'MembershipPutCards',
    # Deliveryaddress
    'DeliveryaddressDelete', 'DeliveryaddressGet', 'DeliveryaddressPost', 'DeliveryaddressPut',
    # Profitpoints
    'ProfitpointsGet', 'ProfitpointsPost',
    # Pricelists
    'PricelistsGetClients', 'PricelistsPutClients', 'PricelistsDelete', 'PricelistsGet',
    'PricelistsPost', 'PricelistsPut', 'PricelistsGetProducts', 'PricelistsPutProducts',
    'PricelistsPutRename',
    # Giftcards
    'GiftcardsPutBlock', 'GiftcardsDelete', 'GiftcardsPost', 'GiftcardsPut', 'GiftcardsSearch',
    'GiftcardsGetTypes', 'GiftcardsPutUnblock',
    # Vouchers
    'VouchersPutBlock', 'VouchersGetTypes', 'VouchersPutUnblock', 'VouchersDelete', 'VouchersGet',
    'VouchersPost', 'VouchersPut',
    # Tags
    'TagsDeleteClear', 'TagsDelete', 'TagsGet', 'TagsPost', 'TagsPut',
    # Payeraddress
    'PayeraddressDelete', 'PayeraddressGet', 'PayeraddressPost', 'PayeraddressPut',
    # Discounts
    'DiscountsGetGroupsClients', 'DiscountsDeleteGroups', 'DiscountsGetGroups', 'DiscountsPostGroups',
    'DiscountsPutGroups', 'DiscountsDeleteGroupsProducts', 'DiscountsPutGroupsProducts',
    'DiscountsPutRebatesBlockCard', 'DiscountsDeleteRebatesCard', 'DiscountsPostRebatesCard',
    'DiscountsDeleteRebatesCode', 'DiscountsPostRebatesCode', 'DiscountsPutRebatesUnblockCard',
    # Newsletter
    'NewsletterSearchEmail', 'NewsletterSearchSms',
    # Clients
    'ClientsGetBalance', 'ClientsPostBalance', 'ClientsGet', 'ClientsPost', 'ClientsPut',
    # CRM
    'CrmSearch',
    # Provincelist
    'ProvincelistGet'
]
