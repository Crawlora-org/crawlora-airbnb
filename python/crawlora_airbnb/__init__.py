"""Typed Airbnb client for the Crawlora hosted API."""

from .platform import AirbnbClient, AsyncAirbnbClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = AirbnbClient
AsyncClient = AsyncAirbnbClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Airbnb'
PLATFORM = 'airbnb'
CONTRACT_REVISION = 'sha256:61a1ad73fe479c52ca215e96b96cec162918a29a197668cc611c7d5309f97a6a'

__all__ = [
    "AirbnbClient", "AsyncAirbnbClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
