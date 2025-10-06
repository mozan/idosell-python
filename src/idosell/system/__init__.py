# Shops
from .shops import GetCurrencies as ShopsGetCurrencies
from .shops import GetLanguages as ShopsGetLanguages

# Deliveries
from .deliveries import PutDefaultProfiles as DeliveriesPutDefaultProfiles
from .deliveries import GetProfiles as DeliveriesGetProfiles
from .deliveries import GetRegions as DeliveriesGetRegions
from .deliveries import PostRegions as DeliveriesPostRegions

# Couriers
from .couriers import GetAssignedToShippingProfiles as CouriersGetAssignedToShippingProfiles
from .couriers import Get as CouriersGet
from .couriers import DeletePickupPoint as CouriersDeletePickupPoint
from .couriers import GetPickupPoints as CouriersGetPickupPoints
from .couriers import PostPickupPoints as CouriersPostPickupPoints
from .couriers import PutPickupPoints as CouriersPutPickupPoints

# System
from .system import GetConfig as SystemGetConfig
from .system import PutConfig as SystemPutConfig
from .system import GetCurrencies as SystemGetCurrencies
from .system import PutCurrencies as SystemPutCurrencies
from .system import GetProcessesAutomation as SystemGetProcessesAutomation
from .system import PutProcessesAutomation as SystemPutProcessesAutomation
from .system import GetServerLoad as SystemGetServerLoad
from .system import GetServerTime as SystemGetServerTime
from .system import GetShopsData as SystemGetShopsData
from .system import GetUnits as SystemGetUnits
from .system import PutUnits as SystemPutUnits
from .system import GetUsers as SystemGetUsers

__all__ = [
    # Shops
    'ShopsGetCurrencies', 'ShopsGetLanguages',
    # Deliveries
    'DeliveriesPutDefaultProfiles', 'DeliveriesGetProfiles', 'DeliveriesGetRegions', 'DeliveriesPostRegions',
    # Couriers
    'CouriersGetAssignedToShippingProfiles', 'CouriersGet', 'CouriersDeletePickupPoint',
    'CouriersGetPickupPoints', 'CouriersPostPickupPoints', 'CouriersPutPickupPoints',
    # System
    'SystemGetConfig', 'SystemPutConfig', 'SystemGetCurrencies', 'SystemPutCurrencies',
    'SystemGetProcessesAutomation', 'SystemPutProcessesAutomation', 'SystemGetServerLoad',
    'SystemGetServerTime', 'SystemGetShopsData', 'SystemGetUnits', 'SystemPutUnits', 'SystemGetUsers'
]
