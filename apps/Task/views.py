from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.Task.serializers import TaskSerializer, InventoryTaskSerializer, EquipmentsTaskSerializer, EmployeesTaskSerializer
from apps.Task.models import Task, Inventory_Task, Equipments_Task, Employee_assigned_Task

# Create your views here.
class EmployeeAssignedTaskViewSet(ModelViewSet):
 queryset = Employee_assigned_Task.objects.all()
 serializer_class = EmployeesTaskSerializer

class InventoryTaskViewSet(ModelViewSet):
 queryset = Inventory_Task.objects.all()
 serializer_class = InventoryTaskSerializer

class EquipmentsTaskViewSet(ModelViewSet):
 queryset = Equipments_Task.objects.all()
 serializer_class = EquipmentsTaskSerializer

class TaskViewSet(ModelViewSet):
 queryset = Task.objects.all()
 serializer_class = TaskSerializer
 