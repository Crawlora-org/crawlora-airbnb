from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelAirbnbSearchResponse = TypedDict('ModelAirbnbSearchResponse', {
    'location': NotRequired[str],
    'page': NotRequired[int],
    'results': NotRequired[list[ModelAirbnbListingItem]],
}, total=False)

ModelAirbnbListingItem = TypedDict('ModelAirbnbListingItem', {
    'host': NotRequired[str],
    'host_id': NotRequired[str],
    'id': NotRequired[str],
    'image': NotRequired[str],
    'is_guest_favorite': NotRequired[bool],
    'is_superhost': NotRequired[bool],
    'latitude': NotRequired[float],
    'location': NotRequired[str],
    'longitude': NotRequired[float],
    'price': NotRequired[float],
    'price_per_night': NotRequired[float],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelAirbnbReviewsResponse = TypedDict('ModelAirbnbReviewsResponse', {
    'id': NotRequired[str],
    'page': NotRequired[int],
    'reviews': NotRequired[list[ModelAirbnbReviewItem]],
}, total=False)

ModelAirbnbReviewItem = TypedDict('ModelAirbnbReviewItem', {
    'author': NotRequired[str],
    'date': NotRequired[str],
    'rating': NotRequired[float],
    'text': NotRequired[str],
}, total=False)

ModelAirbnbCalendarResponse = TypedDict('ModelAirbnbCalendarResponse', {
    'id': NotRequired[str],
    'months': NotRequired[list[ModelAirbnbCalendarMonth]],
}, total=False)

ModelAirbnbCalendarMonth = TypedDict('ModelAirbnbCalendarMonth', {
    'days': NotRequired[list[ModelAirbnbCalendarDay]],
    'month': NotRequired[str],
    'year': NotRequired[int],
}, total=False)

ModelAirbnbCalendarDay = TypedDict('ModelAirbnbCalendarDay', {
    'available': NotRequired[bool],
    'available_for_checkin': NotRequired[bool],
    'available_for_checkout': NotRequired[bool],
    'bookable': NotRequired[bool],
    'date': NotRequired[str],
    'max_nights': NotRequired[int],
    'min_nights': NotRequired[int],
}, total=False)

ModelAirbnbRoomResponse = TypedDict('ModelAirbnbRoomResponse', {
    'amenities': NotRequired[list[str]],
    'description': NotRequired[str],
    'host': NotRequired[str],
    'host_id': NotRequired[str],
    'id': NotRequired[str],
    'image': NotRequired[str],
    'is_guest_favorite': NotRequired[bool],
    'is_superhost': NotRequired[bool],
    'latitude': NotRequired[float],
    'location': NotRequired[str],
    'longitude': NotRequired[float],
    'person_capacity': NotRequired[int],
    'price': NotRequired[float],
    'price_per_night': NotRequired[float],
    'property_type': NotRequired[str],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelAirbnbHostReviewsResponse = TypedDict('ModelAirbnbHostReviewsResponse', {
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'page': NotRequired[int],
    'reviews': NotRequired[list[ModelAirbnbHostReview]],
}, total=False)

ModelAirbnbHostReview = TypedDict('ModelAirbnbHostReview', {
    'comments': NotRequired[str],
    'created_at': NotRequired[str],
    'id': NotRequired[str],
    'rating': NotRequired[float],
    'reviewer': NotRequired[str],
    'reviewer_location': NotRequired[str],
}, total=False)

ModelAirbnbHostListingsResponse = TypedDict('ModelAirbnbHostListingsResponse', {
    'has_more': NotRequired[bool],
    'id': NotRequired[str],
    'listings': NotRequired[list[ModelAirbnbHostListing]],
    'page': NotRequired[int],
}, total=False)

ModelAirbnbHostListing = TypedDict('ModelAirbnbHostListing', {
    'bathrooms': NotRequired[float],
    'bedrooms': NotRequired[int],
    'beds': NotRequired[int],
    'id': NotRequired[str],
    'image': NotRequired[str],
    'instant_book': NotRequired[bool],
    'is_luxury': NotRequired[bool],
    'is_new_listing': NotRequired[bool],
    'is_superhost': NotRequired[bool],
    'name': NotRequired[str],
    'property_type': NotRequired[str],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'room_category': NotRequired[str],
    'room_type': NotRequired[str],
}, total=False)

ModelAirbnbHostResponse = TypedDict('ModelAirbnbHostResponse', {
    'about': NotRequired[str],
    'hosting_years': NotRequired[int],
    'id': NotRequired[str],
    'identity_verified': NotRequired[bool],
    'image': NotRequired[str],
    'interests': NotRequired[list[str]],
    'is_home_host': NotRequired[bool],
    'is_superhost': NotRequired[bool],
    'listing_count': NotRequired[int],
    'location': NotRequired[str],
    'member_years': NotRequired[int],
    'name': NotRequired[str],
    'review_count': NotRequired[int],
    'url': NotRequired[str],
    'verifications': NotRequired[list[str]],
}, total=False)

AirbnbHostResponse = ModelAirbnbHostResponse
AirbnbHostParams = TypedDict('AirbnbHostParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

AirbnbHostListingsResponse = ModelAirbnbHostListingsResponse
AirbnbHostListingsParams = TypedDict('AirbnbHostListingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

AirbnbHostReviewsResponse = ModelAirbnbHostReviewsResponse
AirbnbHostReviewsParams = TypedDict('AirbnbHostReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

AirbnbRoomResponse = ModelAirbnbRoomResponse
AirbnbRoomParams = TypedDict('AirbnbRoomParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

AirbnbRoomCalendarResponse = ModelAirbnbCalendarResponse
AirbnbRoomCalendarParams = TypedDict('AirbnbRoomCalendarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

AirbnbRoomReviewsResponse = ModelAirbnbReviewsResponse
AirbnbRoomReviewsParams = TypedDict('AirbnbRoomReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

AirbnbSearchResponse = ModelAirbnbSearchResponse
AirbnbSearchParams = TypedDict('AirbnbSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'location': Required[str],
    'check_in': NotRequired[str],
    'check_out': NotRequired[str],
    'adults': NotRequired[int],
    'page': NotRequired[int],
    'currency': NotRequired[str],
    'ne_lat': NotRequired[float],
    'ne_lng': NotRequired[float],
    'sw_lat': NotRequired[float],
    'sw_lng': NotRequired[float],
    'zoom': NotRequired[int],
}, total=False)

class AirbnbGroup:
    @overload
    def host(self, **params: Unpack[AirbnbHostStreamParams]) -> BinaryIO: ...
    @overload
    def host(self, **params: Unpack[AirbnbHostTextResponseParams]) -> str: ...
    @overload
    def host(self, **params: Unpack[AirbnbHostDefaultParams]) -> AirbnbHostResponse: ...
    @overload
    def host_listings(self, **params: Unpack[AirbnbHostListingsStreamParams]) -> BinaryIO: ...
    @overload
    def host_listings(self, **params: Unpack[AirbnbHostListingsTextResponseParams]) -> str: ...
    @overload
    def host_listings(self, **params: Unpack[AirbnbHostListingsDefaultParams]) -> AirbnbHostListingsResponse: ...
    @overload
    def host_reviews(self, **params: Unpack[AirbnbHostReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def host_reviews(self, **params: Unpack[AirbnbHostReviewsTextResponseParams]) -> str: ...
    @overload
    def host_reviews(self, **params: Unpack[AirbnbHostReviewsDefaultParams]) -> AirbnbHostReviewsResponse: ...
    @overload
    def room(self, **params: Unpack[AirbnbRoomStreamParams]) -> BinaryIO: ...
    @overload
    def room(self, **params: Unpack[AirbnbRoomTextResponseParams]) -> str: ...
    @overload
    def room(self, **params: Unpack[AirbnbRoomDefaultParams]) -> AirbnbRoomResponse: ...
    @overload
    def room_calendar(self, **params: Unpack[AirbnbRoomCalendarStreamParams]) -> BinaryIO: ...
    @overload
    def room_calendar(self, **params: Unpack[AirbnbRoomCalendarTextResponseParams]) -> str: ...
    @overload
    def room_calendar(self, **params: Unpack[AirbnbRoomCalendarDefaultParams]) -> AirbnbRoomCalendarResponse: ...
    @overload
    def room_reviews(self, **params: Unpack[AirbnbRoomReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def room_reviews(self, **params: Unpack[AirbnbRoomReviewsTextResponseParams]) -> str: ...
    @overload
    def room_reviews(self, **params: Unpack[AirbnbRoomReviewsDefaultParams]) -> AirbnbRoomReviewsResponse: ...
    @overload
    def search(self, **params: Unpack[AirbnbSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[AirbnbSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[AirbnbSearchDefaultParams]) -> AirbnbSearchResponse: ...

OperationId = Literal[
    'airbnb-host',
    'airbnb-host-listings',
    'airbnb-host-reviews',
    'airbnb-room',
    'airbnb-room-calendar',
    'airbnb-room-reviews',
    'airbnb-search',
]

class CrawloraClient:
    airbnb: AirbnbGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['airbnb-host'],
        params: AirbnbHostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbHostResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['airbnb-host-listings'],
        params: AirbnbHostListingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbHostListingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['airbnb-host-reviews'],
        params: AirbnbHostReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbHostReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['airbnb-room'],
        params: AirbnbRoomParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbRoomResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['airbnb-room-calendar'],
        params: AirbnbRoomCalendarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbRoomCalendarResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['airbnb-room-reviews'],
        params: AirbnbRoomReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbRoomReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['airbnb-search'],
        params: AirbnbSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['airbnb-host'],
        params: AirbnbHostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbHostResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['airbnb-host-listings'],
        params: AirbnbHostListingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbHostListingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['airbnb-host-reviews'],
        params: AirbnbHostReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbHostReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['airbnb-room'],
        params: AirbnbRoomParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbRoomResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['airbnb-room-calendar'],
        params: AirbnbRoomCalendarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbRoomCalendarResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['airbnb-room-reviews'],
        params: AirbnbRoomReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbRoomReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['airbnb-search'],
        params: AirbnbSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AirbnbSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class AirbnbClient(CrawloraClient):
    def __enter__(self) -> AirbnbClient: ...
    @overload
    def host(self, **params: Unpack[AirbnbHostStreamParams]) -> BinaryIO: ...
    @overload
    def host(self, **params: Unpack[AirbnbHostTextResponseParams]) -> str: ...
    @overload
    def host(self, **params: Unpack[AirbnbHostDefaultParams]) -> AirbnbHostResponse: ...
    @overload
    def host_listings(self, **params: Unpack[AirbnbHostListingsStreamParams]) -> BinaryIO: ...
    @overload
    def host_listings(self, **params: Unpack[AirbnbHostListingsTextResponseParams]) -> str: ...
    @overload
    def host_listings(self, **params: Unpack[AirbnbHostListingsDefaultParams]) -> AirbnbHostListingsResponse: ...
    @overload
    def host_reviews(self, **params: Unpack[AirbnbHostReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def host_reviews(self, **params: Unpack[AirbnbHostReviewsTextResponseParams]) -> str: ...
    @overload
    def host_reviews(self, **params: Unpack[AirbnbHostReviewsDefaultParams]) -> AirbnbHostReviewsResponse: ...
    @overload
    def room(self, **params: Unpack[AirbnbRoomStreamParams]) -> BinaryIO: ...
    @overload
    def room(self, **params: Unpack[AirbnbRoomTextResponseParams]) -> str: ...
    @overload
    def room(self, **params: Unpack[AirbnbRoomDefaultParams]) -> AirbnbRoomResponse: ...
    @overload
    def room_calendar(self, **params: Unpack[AirbnbRoomCalendarStreamParams]) -> BinaryIO: ...
    @overload
    def room_calendar(self, **params: Unpack[AirbnbRoomCalendarTextResponseParams]) -> str: ...
    @overload
    def room_calendar(self, **params: Unpack[AirbnbRoomCalendarDefaultParams]) -> AirbnbRoomCalendarResponse: ...
    @overload
    def room_reviews(self, **params: Unpack[AirbnbRoomReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def room_reviews(self, **params: Unpack[AirbnbRoomReviewsTextResponseParams]) -> str: ...
    @overload
    def room_reviews(self, **params: Unpack[AirbnbRoomReviewsDefaultParams]) -> AirbnbRoomReviewsResponse: ...
    @overload
    def search(self, **params: Unpack[AirbnbSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[AirbnbSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[AirbnbSearchDefaultParams]) -> AirbnbSearchResponse: ...

class AsyncAirbnbClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncAirbnbClient: ...
    airbnb: _AsyncAirbnbGroup
    @overload
    async def host(self, **params: Unpack[AirbnbHostStreamParams]) -> BinaryIO: ...
    @overload
    async def host(self, **params: Unpack[AirbnbHostTextResponseParams]) -> str: ...
    @overload
    async def host(self, **params: Unpack[AirbnbHostDefaultParams]) -> AirbnbHostResponse: ...
    @overload
    async def host_listings(self, **params: Unpack[AirbnbHostListingsStreamParams]) -> BinaryIO: ...
    @overload
    async def host_listings(self, **params: Unpack[AirbnbHostListingsTextResponseParams]) -> str: ...
    @overload
    async def host_listings(self, **params: Unpack[AirbnbHostListingsDefaultParams]) -> AirbnbHostListingsResponse: ...
    @overload
    async def host_reviews(self, **params: Unpack[AirbnbHostReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def host_reviews(self, **params: Unpack[AirbnbHostReviewsTextResponseParams]) -> str: ...
    @overload
    async def host_reviews(self, **params: Unpack[AirbnbHostReviewsDefaultParams]) -> AirbnbHostReviewsResponse: ...
    @overload
    async def room(self, **params: Unpack[AirbnbRoomStreamParams]) -> BinaryIO: ...
    @overload
    async def room(self, **params: Unpack[AirbnbRoomTextResponseParams]) -> str: ...
    @overload
    async def room(self, **params: Unpack[AirbnbRoomDefaultParams]) -> AirbnbRoomResponse: ...
    @overload
    async def room_calendar(self, **params: Unpack[AirbnbRoomCalendarStreamParams]) -> BinaryIO: ...
    @overload
    async def room_calendar(self, **params: Unpack[AirbnbRoomCalendarTextResponseParams]) -> str: ...
    @overload
    async def room_calendar(self, **params: Unpack[AirbnbRoomCalendarDefaultParams]) -> AirbnbRoomCalendarResponse: ...
    @overload
    async def room_reviews(self, **params: Unpack[AirbnbRoomReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def room_reviews(self, **params: Unpack[AirbnbRoomReviewsTextResponseParams]) -> str: ...
    @overload
    async def room_reviews(self, **params: Unpack[AirbnbRoomReviewsDefaultParams]) -> AirbnbRoomReviewsResponse: ...
    @overload
    async def search(self, **params: Unpack[AirbnbSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[AirbnbSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[AirbnbSearchDefaultParams]) -> AirbnbSearchResponse: ...

class _AsyncAirbnbGroup:
    @overload
    async def host(self, **params: Unpack[AirbnbHostStreamParams]) -> BinaryIO: ...
    @overload
    async def host(self, **params: Unpack[AirbnbHostTextResponseParams]) -> str: ...
    @overload
    async def host(self, **params: Unpack[AirbnbHostDefaultParams]) -> AirbnbHostResponse: ...
    @overload
    async def host_listings(self, **params: Unpack[AirbnbHostListingsStreamParams]) -> BinaryIO: ...
    @overload
    async def host_listings(self, **params: Unpack[AirbnbHostListingsTextResponseParams]) -> str: ...
    @overload
    async def host_listings(self, **params: Unpack[AirbnbHostListingsDefaultParams]) -> AirbnbHostListingsResponse: ...
    @overload
    async def host_reviews(self, **params: Unpack[AirbnbHostReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def host_reviews(self, **params: Unpack[AirbnbHostReviewsTextResponseParams]) -> str: ...
    @overload
    async def host_reviews(self, **params: Unpack[AirbnbHostReviewsDefaultParams]) -> AirbnbHostReviewsResponse: ...
    @overload
    async def room(self, **params: Unpack[AirbnbRoomStreamParams]) -> BinaryIO: ...
    @overload
    async def room(self, **params: Unpack[AirbnbRoomTextResponseParams]) -> str: ...
    @overload
    async def room(self, **params: Unpack[AirbnbRoomDefaultParams]) -> AirbnbRoomResponse: ...
    @overload
    async def room_calendar(self, **params: Unpack[AirbnbRoomCalendarStreamParams]) -> BinaryIO: ...
    @overload
    async def room_calendar(self, **params: Unpack[AirbnbRoomCalendarTextResponseParams]) -> str: ...
    @overload
    async def room_calendar(self, **params: Unpack[AirbnbRoomCalendarDefaultParams]) -> AirbnbRoomCalendarResponse: ...
    @overload
    async def room_reviews(self, **params: Unpack[AirbnbRoomReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def room_reviews(self, **params: Unpack[AirbnbRoomReviewsTextResponseParams]) -> str: ...
    @overload
    async def room_reviews(self, **params: Unpack[AirbnbRoomReviewsDefaultParams]) -> AirbnbRoomReviewsResponse: ...
    @overload
    async def search(self, **params: Unpack[AirbnbSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[AirbnbSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[AirbnbSearchDefaultParams]) -> AirbnbSearchResponse: ...

AirbnbHostDefaultParams = TypedDict('AirbnbHostDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

AirbnbHostTextResponseParams = TypedDict('AirbnbHostTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

AirbnbHostStreamParams = TypedDict('AirbnbHostStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

AirbnbHostListingsDefaultParams = TypedDict('AirbnbHostListingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

AirbnbHostListingsTextResponseParams = TypedDict('AirbnbHostListingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

AirbnbHostListingsStreamParams = TypedDict('AirbnbHostListingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

AirbnbHostReviewsDefaultParams = TypedDict('AirbnbHostReviewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

AirbnbHostReviewsTextResponseParams = TypedDict('AirbnbHostReviewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

AirbnbHostReviewsStreamParams = TypedDict('AirbnbHostReviewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

AirbnbRoomDefaultParams = TypedDict('AirbnbRoomDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

AirbnbRoomTextResponseParams = TypedDict('AirbnbRoomTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

AirbnbRoomStreamParams = TypedDict('AirbnbRoomStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

AirbnbRoomCalendarDefaultParams = TypedDict('AirbnbRoomCalendarDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

AirbnbRoomCalendarTextResponseParams = TypedDict('AirbnbRoomCalendarTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

AirbnbRoomCalendarStreamParams = TypedDict('AirbnbRoomCalendarStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

AirbnbRoomReviewsDefaultParams = TypedDict('AirbnbRoomReviewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

AirbnbRoomReviewsTextResponseParams = TypedDict('AirbnbRoomReviewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

AirbnbRoomReviewsStreamParams = TypedDict('AirbnbRoomReviewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

AirbnbSearchDefaultParams = TypedDict('AirbnbSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'location': Required[str],
    'check_in': NotRequired[str],
    'check_out': NotRequired[str],
    'adults': NotRequired[int],
    'page': NotRequired[int],
    'currency': NotRequired[str],
    'ne_lat': NotRequired[float],
    'ne_lng': NotRequired[float],
    'sw_lat': NotRequired[float],
    'sw_lng': NotRequired[float],
    'zoom': NotRequired[int],
}, total=False)

AirbnbSearchTextResponseParams = TypedDict('AirbnbSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'location': Required[str],
    'check_in': NotRequired[str],
    'check_out': NotRequired[str],
    'adults': NotRequired[int],
    'page': NotRequired[int],
    'currency': NotRequired[str],
    'ne_lat': NotRequired[float],
    'ne_lng': NotRequired[float],
    'sw_lat': NotRequired[float],
    'sw_lng': NotRequired[float],
    'zoom': NotRequired[int],
}, total=False)

AirbnbSearchStreamParams = TypedDict('AirbnbSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'location': Required[str],
    'check_in': NotRequired[str],
    'check_out': NotRequired[str],
    'adults': NotRequired[int],
    'page': NotRequired[int],
    'currency': NotRequired[str],
    'ne_lat': NotRequired[float],
    'ne_lng': NotRequired[float],
    'sw_lat': NotRequired[float],
    'sw_lng': NotRequired[float],
    'zoom': NotRequired[int],
}, total=False)
