from rest_framework.serializers import ModelSerializer
from apps.Task.models import Task, Employee_assigned_Task, Inventory_Task, Equipments_Task


class EmployeesTaskSerializer(ModelSerializer):
 class Meta:
    model = Employee_assigned_Task
    fields = '__all__'


class InventoryTaskSerializer(ModelSerializer):
  class Meta:
    model = Inventory_Task
    fields = '__all__'
 

class EquipmentsTaskSerializer(ModelSerializer):
 class Meta:
    model = Equipments_Task
    fields = '__all__'


class TaskSerializer(ModelSerializer):
 class Meta:
    model = Task
    fields = '__all__'
