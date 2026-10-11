import { AirbnbClient } from "../src/index.js";

const client = new AirbnbClient({ apiKey: "test-key" });
void client.host({"id": "sample"});
void client.request("airbnb-host", {"id": "sample"});
const streamResponse: Promise<Response> = client.request("airbnb-host", {"id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("airbnb-host", {"id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.host({"id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("airbnb-host", {"id": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("airbnb-host", {"id": "sample"}, { responseType: "text" });
void rawText;



// @ts-expect-error The selected operation requires its documented params.
void client.host();
