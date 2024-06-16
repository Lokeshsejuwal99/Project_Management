import asyncio
import json
from uuid import UUID
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrTimeout, ErrConnectionClosed


def serialize_uuid(obj):
    if isinstance(obj, UUID):
        return str(obj)
    raise TypeError(f"Object of type {type(obj)} is not a JSON serializable..")


async def publish_event(subject, data):
    ns = NATS()
    max_retires = 3
    for attempt in range(max_retires):
        try:
            await ns.connect("nats://localhost:4222", connect_timeout=10)
            await ns.publish(subject, json.dumps(data, default=serialize_uuid).encode())
            break
        except ErrConnectionClosed:
            print("Error: Connection to NATS server is closed !!!!!")

        except ErrTimeout:
            print(f"Connection to the NATS server timed out. Attemp {attempt + 1} of {max_retires}.")
        finally:
            await ns.close()
        await asyncio.sleep(2 ** attempt)
 

async def publish_inventory_created(inventory_data):
    print(f"Inventory.created' event is published with data: {inventory_data}")
    await publish_event("inventory.created", inventory_data)


async def publish_inventory_updated(equipment_data):
    print(f"Inventory.updated' event is published with data: {equipment_data}")
    await publish_event("inventory.updated", equipment_data)


async def publish_inventory_deleted(equipment_data):
    print("Inventory.deleted event is published successfully.")
    await publish_event("inventory.deleted", equipment_data)

 
async def publish_equipment_created(equipment_data):
    print(f"Equipment.created' event is published with data: {equipment_data}")
    await publish_event("inventory.created", equipment_data)


async def publish_equipment_updated(equipment_data):
    print(f"Equipment.updated' event is published with data: {equipment_data}")
    await publish_event("inventory.updated", equipment_data)


async def publish_equipment_deleted(equipment_data):
    print("Equipment.deleted event is published successfully.")
    await publish_event("inventory.deleted", equipment_data)