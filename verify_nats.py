import asyncio
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout


async def verify_connection():
    ns = NATS()
    try:
        await ns.connect("nats://localhost:4222", connect_timeout=10)
        print("Successfully connected to NATS server. ")
    except ErrTimeout:
        print("Connection to nats server timed out.")
    finally:
        await ns.close()

asyncio.run(verify_connection())
