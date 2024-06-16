import asyncio
from nats.aio.client import Client as NATS

'''Async func for inventory subscribe.'''


async def inventory_created_subscriber(msg):
    data = msg.data.decode()
    print(f"Received an inventory Created message: {data}")


async def inventory_updated_subscriber(msg):
    data = msg.data.decode()
    print(f"Received an inventory updated message: {data}")


async def inventory_deleted_subscriber(msg):
    data = msg.data.decode()
    print(f"Received an inventory deleted message: {data}")


'''Async func for equipment subscribe.'''


async def equipment_created_subscriber(msg):
    data = msg.data.decode()
    print(f"Received an equipment Created message: {data}")


async def equipment_updated_subscriber(msg):
    data = msg.data.decode()
    print(f"Received an equipment updated message: {data}")


async def equipment_deleted_subscriber(msg):
    data = msg.data.decode()
    print(f"Received an equipment deleted message: {data}")


async def run():
    ns = NATS()
    await ns.connect("https://127.0.0.1:4222")

    # Subscribe to the different event of an inventory
    await ns.subscribe("inventory.created", cb=inventory_created_subscriber)
    await ns.subscribe("inventory.updated", cb=inventory_updated_subscriber)
    await ns.subscribe("inventory.deleted", cb=inventory_deleted_subscriber)
    await ns.subscribe("equipment.created", cb=equipment_created_subscriber)
    await ns.subscribe("equipment.updated", cb=equipment_updated_subscriber)
    await ns.subscribe("equipment.deleted", cb=equipment_deleted_subscriber)
    
    print("Listening for the events of a resources......")

    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(run())