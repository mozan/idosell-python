# Campaign
from .campaign import Get as CampaignGet
from .campaign import Post as CampaignPost
from .campaign import Put as CampaignPut
from .campaign import Delete as CampaignDelete

# Snippets
from .snippets import Get as SnippetsGet
from .snippets import Post as SnippetsPost
from .snippets import Put as SnippetsPut
from .snippets import Delete as SnippetsDelete

# Cookies
from .cookies import Get as CookiesGet
from .cookies import Post as CookiesPost
from .cookies import Put as CookiesPut
from .cookies import Delete as CookiesDelete

__all__ = [
    # Campaign
    'CampaignGet', 'CampaignPost', 'CampaignPut', 'CampaignDelete',
    # Snippets
    'SnippetsGet', 'SnippetsPost', 'SnippetsPut', 'SnippetsDelete',
    # Cookies
    'CookiesGet', 'CookiesPost', 'CookiesPut', 'CookiesDelete'
]
