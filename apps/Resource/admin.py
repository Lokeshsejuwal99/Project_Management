from django.contrib import admin
from .models import Inventory, Equipments, Employee_assigned

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Equipments)
admin.site.register(Employee_assigned)