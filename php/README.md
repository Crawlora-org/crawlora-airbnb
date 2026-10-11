# Crawlora Airbnb API client for PHP (`crawlora/airbnb`)

This PHP package calls Crawlora's hosted Airbnb API at `https://api.crawlora.net/api/v1`. It exposes 7 endpoints covering listing search, room details, calendars and reviews, and host profiles, listings and reviews. It does not call or scrape Airbnb directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/airbnb
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Airbnb\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("airbnb-search", ['location' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 7 API operations.

## Supported Airbnb API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-airbnb/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/airbnb/host/{id}` | `airbnb-host` | Get Airbnb host profile |
| `GET` | `/airbnb/host/{id}/listings` | `airbnb-host-listings` | Get Airbnb host listings |
| `GET` | `/airbnb/host/{id}/reviews` | `airbnb-host-reviews` | Get Airbnb host reviews |
| `GET` | `/airbnb/room/{id}` | `airbnb-room` | Get Airbnb room |
| `GET` | `/airbnb/room/{id}/calendar` | `airbnb-room-calendar` | Get Airbnb room calendar |
| `GET` | `/airbnb/room/{id}/reviews` | `airbnb-room-reviews` | Get Airbnb room reviews |
| `GET` | `/airbnb/search` | `airbnb-search` | Search Airbnb stays |

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-airbnb). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-airbnb/blob/main/docs/usage.md).
