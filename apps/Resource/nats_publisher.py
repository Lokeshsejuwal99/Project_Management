from nats.aio.client import Client as NATS
import asyncio
from django.conf import settings

async def publish_inventory_created_event(inventory):
    nc = NATS()

    try:
        await nc.connect(servers=settings.NATS_SERVERS)  # Update with your NATS server details

        subject = "inventory.created"
        # Example payload including all fields of the inventory model
        data = {
            "id": inventory.id,
            "name": inventory.Name,
            "quantity": inventory.Quantity,
            "size": inventory.size,
            "client_name": inventory.Client_name,
            "address": inventory.Address,
            "phone": inventory.Phone,
            "email": inventory.Email
        }

        await nc.publish(subject, data)
        print(f"Published inventory created event for inventory: {inventory.Name}")

    finally:
        await nc.close()
