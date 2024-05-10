from nats.aio.client import Client as NATS
import asyncio
from django.conf import settings
from Project.models import Project
from Resource.models import Inventory 
# Import your Project model here

async def handle_inventory_created_event(msg):
    subject = msg.subject
    data = msg.data.decode()

    # Process the received data
    # Assuming data contains the ID of the created inventory item
    inventory_id = int(data)

    # Retrieve the inventory object using the ID
    try:
        inventory = Inventory.objects.get(id=inventory_id)
    except Inventory.DoesNotExist:
        print(f"Inventory with ID {inventory_id} and subject of {subject} does not exist.")
        return

    # Update the projects that are associated with this inventory
    projects = Project.objects.filter(inventory=inventory)
    for project in projects:
        # Add your logic here to update the project based on the new inventory
        print(f"Updating project '{project.Name}' with new inventory '{inventory.Name}'")

async def run(loop):
    nc = NATS()

    try:
        await nc.connect(servers=settings.NATS_SERVERS)

        # Subscribe to the 'inventory.created' subject
        await nc.subscribe("inventory.created", cb=handle_inventory_created_event)

        # Keep the connection open
        await asyncio.sleep(1)

    finally:
        await nc.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
