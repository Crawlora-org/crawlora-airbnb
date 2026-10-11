import { AirbnbClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new AirbnbClient({ apiKey });

  const search = await client.search({ location: "Lisbon, Portugal" });
  console.log("search", search);
  const room = await client.room({ id: "7743405" });
  console.log("room", room);
