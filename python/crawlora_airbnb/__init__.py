"""Typed Airbnb client for the Crawlora hosted API."""

from .platform import AirbnbClient, AsyncAirbnbClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = AirbnbClient
AsyncClient = AsyncAirbnbClient
__version__ = '0.1.2'
DISPLAY_NAME = 'Airbnb'
PLATFORM = 'airbnb'
CONTRACT_REVISION = 'sha256:87210a3d0e9a34255a495ce152452e7f72300ed84e8c573ffd615b5ac335a93b'

__all__ = [
    "AirbnbClient", "AsyncAirbnbClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
