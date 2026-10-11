import os

from crawlora_airbnb import AirbnbClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with AirbnbClient(api_key=api_key) as client:
    search = client.search(location='Lisbon, Portugal')
    print('search', search)
    room = client.room(id='7743405')
    print('room', room)
