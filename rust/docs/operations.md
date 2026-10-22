# Crawlora Airbnb Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `7`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| airbnb | `airbnb.host` | `airbnb-host` | `GET /airbnb/host/{id}` | `id` (path String required) | `ApiKeyAuth` | `AirbnbHostResponse` |  |
| airbnb | `airbnb.host_listings` | `airbnb-host-listings` | `GET /airbnb/host/{id}/listings` | `id` (path String required)<br>`page` (query i64) | `ApiKeyAuth` | `AirbnbHostListingsResponse` |  |
| airbnb | `airbnb.host_reviews` | `airbnb-host-reviews` | `GET /airbnb/host/{id}/reviews` | `id` (path String required)<br>`page` (query i64) | `ApiKeyAuth` | `AirbnbHostReviewsResponse` |  |
| airbnb | `airbnb.room` | `airbnb-room` | `GET /airbnb/room/{id}` | `id` (path String required) | `ApiKeyAuth` | `AirbnbRoomResponse` |  |
| airbnb | `airbnb.room_calendar` | `airbnb-room-calendar` | `GET /airbnb/room/{id}/calendar` | `id` (path String required) | `ApiKeyAuth` | `AirbnbRoomCalendarResponse` |  |
| airbnb | `airbnb.room_reviews` | `airbnb-room-reviews` | `GET /airbnb/room/{id}/reviews` | `id` (path String required)<br>`page` (query i64) | `ApiKeyAuth` | `AirbnbRoomReviewsResponse` |  |
| airbnb | `airbnb.search` | `airbnb-search` | `GET /airbnb/search` | `location` (query String required)<br>`check_in` (query String)<br>`check_out` (query String)<br>`adults` (query i64)<br>`page` (query i64)<br>`currency` (query String)<br>`ne_lat` (query f64)<br>`ne_lng` (query f64)<br>`sw_lat` (query f64)<br>`sw_lng` (query f64)<br>`zoom` (query i64) | `ApiKeyAuth` | `AirbnbSearchResponse` |  |
