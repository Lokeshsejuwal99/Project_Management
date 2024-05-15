from django.contrib import admin
from .models import Task, Equipments_Task, Inventory_Task, Employee_assigned_Task

# Register your models here.
admin.site.register(Task)
admin.site.register(Inventory_Task)
admin.site.register(Employee_assigned_Task)
admin.site.register(Equipments_Task)
