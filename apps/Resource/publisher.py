import asyncio
import pickle
from nats.aio.client import Client as NATS

async def publish_inventory_created_event(inventory):
    inventory=pickle.dumps(inventory)
    nc = NATS()
    try:
        await nc.connect(servers=["nats://localhost:4222"]) 
        subject = "inventory.created"
        await nc.publish(subject, inventory)
        print(f"Published inventory created event for inventory:")
    finally:
        await nc.close()
