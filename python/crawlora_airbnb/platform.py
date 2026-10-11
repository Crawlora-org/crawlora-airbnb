"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class AirbnbClient(CrawloraClient):
    """Synchronous Airbnb API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-airbnb-python/0.1.1')
        super().__init__(*args, **kwargs)

    def host(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('airbnb-host', params, response_type=response_type, timeout=timeout, headers=headers)

    def host_listings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('airbnb-host-listings', params, response_type=response_type, timeout=timeout, headers=headers)

    def host_reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('airbnb-host-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    def room(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('airbnb-room', params, response_type=response_type, timeout=timeout, headers=headers)

    def room_calendar(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('airbnb-room-calendar', params, response_type=response_type, timeout=timeout, headers=headers)

    def room_reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('airbnb-room-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('airbnb-search', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncAirbnbClient(AsyncCrawloraClient):
    """Asynchronous Airbnb API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-airbnb-python/0.1.1')
        super().__init__(*args, **kwargs)

    async def host(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('airbnb-host', params, response_type=response_type, timeout=timeout, headers=headers)

    async def host_listings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('airbnb-host-listings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def host_reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('airbnb-host-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    async def room(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('airbnb-room', params, response_type=response_type, timeout=timeout, headers=headers)

    async def room_calendar(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('airbnb-room-calendar', params, response_type=response_type, timeout=timeout, headers=headers)

    async def room_reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('airbnb-room-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('airbnb-search', params, response_type=response_type, timeout=timeout, headers=headers)
