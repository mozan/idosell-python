# Campaign
from .campaign import Get as CampaignGet
from .campaign import Post as CampaignPost
from .campaign import Put as CampaignPut
from .campaign import Delete as CampaignDelete

# CPA
from .cpa import Get as CpaGet
from .cpa import Post as CpaPost
from .cpa import Put as CpaPut
from .cpa import Delete as CpaDelete

__all__ = [
    # Campaign
    'CampaignGet', 'CampaignPost', 'CampaignPut', 'CampaignDelete',
    # CPA
    'CpaGet', 'CpaPost', 'CpaPut', 'CpaDelete'
]
