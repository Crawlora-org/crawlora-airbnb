import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class AirbnbClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-airbnb-js/0.1.2" });
    this["host"] = (...args) => this.request("airbnb-host", ...args);
    this["hostListings"] = (...args) => this.request("airbnb-host-listings", ...args);
    this["hostReviews"] = (...args) => this.request("airbnb-host-reviews", ...args);
    this["room"] = (...args) => this.request("airbnb-room", ...args);
    this["roomCalendar"] = (...args) => this.request("airbnb-room-calendar", ...args);
    this["roomReviews"] = (...args) => this.request("airbnb-room-reviews", ...args);
    this["search"] = (...args) => this.request("airbnb-search", ...args);
  }
}

export { AirbnbClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.2";
export default AirbnbClient;
