# management/commands/run_nats_subscriber.py
from django.core.management.base import BaseCommand
import asyncio
from Project.nats_subscriber import handle_inventory_created_event

class Command(BaseCommand):
    help = 'Run NATS subscriber to listen for inventory created events'

    def handle(self, *args, **kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(handle_inventory_created_event())
