# @crawlora-org/airbnb — Airbnb API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Airbnb API.
It exposes 7 API endpoints for listing search, room details, calendars and reviews, and host profiles, listings and reviews through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-javascript-homepage). It does not run a browser or scrape Airbnb locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Airbnb or its owners.

## Install

```sh
npm install @crawlora-org/airbnb
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=airbnb-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { AirbnbClient } from "@crawlora-org/airbnb";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new AirbnbClient({ apiKey });
const result1 = await client.search({ location: "Lisbon, Portugal" });
console.log(result1);
const result2 = await client.room({ id: "7743405" });
console.log(result2);
```

The client also exports `Client` as an alias for `AirbnbClient`. Operation
methods are available directly in camelCase and through the `airbnb`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-airbnb/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-airbnb/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Airbnb API endpoints

This package exposes each route below as a direct method and through the `airbnb` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-airbnb/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/airbnb/host/{id}` | `airbnb-host` | Get Airbnb host profile |
| `GET` | `/airbnb/host/{id}/listings` | `airbnb-host-listings` | Get Airbnb host listings |
| `GET` | `/airbnb/host/{id}/reviews` | `airbnb-host-reviews` | Get Airbnb host reviews |
| `GET` | `/airbnb/room/{id}` | `airbnb-room` | Get Airbnb room |
| `GET` | `/airbnb/room/{id}/calendar` | `airbnb-room-calendar` | Get Airbnb room calendar |
| `GET` | `/airbnb/room/{id}/reviews` | `airbnb-room-reviews` | Get Airbnb room reviews |
| `GET` | `/airbnb/search` | `airbnb-search` | Search Airbnb stays |

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
