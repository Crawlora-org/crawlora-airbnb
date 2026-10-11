# Crawlora Airbnb API client for Ruby (`crawlora-airbnb`)

This Ruby gem calls Crawlora's hosted Airbnb API at `https://api.crawlora.net/api/v1`. It exposes 7 endpoints covering listing search, room details, calendars and reviews, and host profiles, listings and reviews; it does not call or scrape Airbnb directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-airbnb"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/airbnb"

client = Crawlora::Airbnb::Client.new
result = client.request("airbnb-search", JSON.parse("{\"location\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 7 API operations.

```ruby
client = Crawlora::Airbnb::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Airbnb API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-airbnb/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/airbnb/host/{id}` | `airbnb-host` | Get Airbnb host profile |
| `GET` | `/airbnb/host/{id}/listings` | `airbnb-host-listings` | Get Airbnb host listings |
| `GET` | `/airbnb/host/{id}/reviews` | `airbnb-host-reviews` | Get Airbnb host reviews |
| `GET` | `/airbnb/room/{id}` | `airbnb-room` | Get Airbnb room |
| `GET` | `/airbnb/room/{id}/calendar` | `airbnb-room-calendar` | Get Airbnb room calendar |
| `GET` | `/airbnb/room/{id}/reviews` | `airbnb-room-reviews` | Get Airbnb room reviews |
| `GET` | `/airbnb/search` | `airbnb-search` | Search Airbnb stays |

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-airbnb) for account setup, the API operation reference, and release history.
