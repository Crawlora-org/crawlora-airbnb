# Crawlora Airbnb JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `7`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| airbnb | `airbnb.host` | `airbnb-host` | `GET /airbnb/host/{id}` | `id` (path string required) | `ApiKeyAuth` | `AirbnbHostResponse` |  |
| airbnb | `airbnb.hostListings` | `airbnb-host-listings` | `GET /airbnb/host/{id}/listings` | `id` (path string required)<br>`page` (query number) | `ApiKeyAuth` | `AirbnbHostListingsResponse` |  |
| airbnb | `airbnb.hostReviews` | `airbnb-host-reviews` | `GET /airbnb/host/{id}/reviews` | `id` (path string required)<br>`page` (query number) | `ApiKeyAuth` | `AirbnbHostReviewsResponse` |  |
| airbnb | `airbnb.room` | `airbnb-room` | `GET /airbnb/room/{id}` | `id` (path string required) | `ApiKeyAuth` | `AirbnbRoomResponse` |  |
| airbnb | `airbnb.roomCalendar` | `airbnb-room-calendar` | `GET /airbnb/room/{id}/calendar` | `id` (path string required) | `ApiKeyAuth` | `AirbnbRoomCalendarResponse` |  |
| airbnb | `airbnb.roomReviews` | `airbnb-room-reviews` | `GET /airbnb/room/{id}/reviews` | `id` (path string required)<br>`page` (query number) | `ApiKeyAuth` | `AirbnbRoomReviewsResponse` |  |
| airbnb | `airbnb.search` | `airbnb-search` | `GET /airbnb/search` | `location` (query string required)<br>`check_in` (query string)<br>`check_out` (query string)<br>`adults` (query number)<br>`page` (query number)<br>`currency` (query string)<br>`ne_lat` (query number)<br>`ne_lng` (query number)<br>`sw_lat` (query number)<br>`sw_lng` (query number)<br>`zoom` (query number) | `ApiKeyAuth` | `AirbnbSearchResponse` |  |
