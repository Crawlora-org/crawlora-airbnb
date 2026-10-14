# Crawlora Airbnb API client for Java

The official Java client for Crawlora's hosted Airbnb API. It exposes 7 endpoints covering listing search, room details, calendars and reviews, and host profiles, listings and reviews. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-airbnb</artifactId>
  <version>0.1.2</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-java-console) to get an API key.

```java
import net.crawlora.airbnb.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.search(Map.ofEntries(Map.entry("location", "Lisbon, Portugal")));
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Airbnb API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-airbnb/blob/main/docs/usage.md) also lists parameters and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/airbnb/host/{id}` | `airbnb-host` | Get Airbnb host profile |
| `GET` | `/airbnb/host/{id}/listings` | `airbnb-host-listings` | Get Airbnb host listings |
| `GET` | `/airbnb/host/{id}/reviews` | `airbnb-host-reviews` | Get Airbnb host reviews |
| `GET` | `/airbnb/room/{id}` | `airbnb-room` | Get Airbnb room |
| `GET` | `/airbnb/room/{id}/calendar` | `airbnb-room-calendar` | Get Airbnb room calendar |
| `GET` | `/airbnb/room/{id}/reviews` | `airbnb-room-reviews` | Get Airbnb room reviews |
| `GET` | `/airbnb/search` | `airbnb-search` | Search Airbnb stays |

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-airbnb)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-java-api-docs)
