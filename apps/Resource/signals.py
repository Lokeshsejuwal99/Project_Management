import asyncio
from django.http import HttpResponse
# inventory/views.py or inventory/signals.py
from .models import Inventory
from .nats_publisher import publish_inventory_created_event


def create_inventory(request):
    # Your inventory creation logic here
    inventory_name = "New Inventory Item"  # Example
    inventory = Inventory.objects.create(name=inventory_name)

    # Publish event to NATS
    asyncio.run(publish_inventory_created_event(inventory_name, inventory))

    return HttpResponse("Inventory created successfully")
