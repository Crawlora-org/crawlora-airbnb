# Airbnb API endpoint reference and client usage

This reference lists all 7 public Airbnb API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/airbnb`, `crawlora-airbnb`, and `crawlora-airbnb` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Airbnb locally; Crawlora is independent from and not endorsed by Airbnb or its owners.

The package tracks the public API contract revision `sha256:87210a3d0e9a34255a495ce152452e7f72300ed84e8c573ffd615b5ac335a93b` bundled with release `0.1.2`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `airbnb`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `host` | `host` | `airbnb.host` | `GET /airbnb/host/{id}` | `id` (path, required) | Get Airbnb host profile |
| `hostListings` | `host_listings` | `airbnb.host_listings` | `GET /airbnb/host/{id}/listings` | `id` (path, required), `page` (query, optional) | Get Airbnb host listings |
| `hostReviews` | `host_reviews` | `airbnb.host_reviews` | `GET /airbnb/host/{id}/reviews` | `id` (path, required), `page` (query, optional) | Get Airbnb host reviews |
| `room` | `room` | `airbnb.room` | `GET /airbnb/room/{id}` | `id` (path, required) | Get Airbnb room |
| `roomCalendar` | `room_calendar` | `airbnb.room_calendar` | `GET /airbnb/room/{id}/calendar` | `id` (path, required) | Get Airbnb room calendar |
| `roomReviews` | `room_reviews` | `airbnb.room_reviews` | `GET /airbnb/room/{id}/reviews` | `id` (path, required), `page` (query, optional) | Get Airbnb room reviews |
| `search` | `search` | `airbnb.search` | `GET /airbnb/search` | `location` (query, required), `check_in` (query, optional), `check_out` (query, optional), `adults` (query, optional), `page` (query, optional), `currency` (query, optional), `ne_lat` (query, optional), `ne_lng` (query, optional), `sw_lat` (query, optional), `sw_lng` (query, optional), `zoom` (query, optional) | Search Airbnb stays |

## Client forms

- JavaScript: import `AirbnbClient` (also exported as `Client`) from `@crawlora-org/airbnb`; use `new AirbnbClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `AirbnbClient` (also exported as `Client`) from `crawlora_airbnb`; use `with AirbnbClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncAirbnbClient`, used with `async with` and `await`.
- Rust: add `crawlora-airbnb` with Cargo; import `Client` and the generated operation parameter struct, then call `client.airbnb.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-airbnb/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
