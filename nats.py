# Import NATS client
from nats.aio.client import Client as NATS

# Initialize NATS client
nats_client = NATS()

# Connect to NATS server (optional)
async def connect_to_nats():
    await nats_client.connect(servers=["nats://localhost:4222"])

# Run the event loop for connecting to NATS server (optional)
async def run_nats_client():
    await connect_to_nats()

# Call the event loop to start the NATS client (optional)
import asyncio
asyncio.get_event_loop().run_until_complete(run_nats_client())
