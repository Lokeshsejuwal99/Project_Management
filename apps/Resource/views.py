from django.shortcuts import render
from .models import  Employee_assigned, Inventory, Equipments
from .serializers import InventorySerializer, EmployeesSerializer, EquipementsTSerializer
from rest_framework.viewsets import ModelViewSet
from Project_main.pagination import CustomPagination

# Create your views here.
class EmployeeViewSet(ModelViewSet):
 queryset = Employee_assigned.objects.all()
 serializer_class = EmployeesSerializer
 pagination_class = CustomPagination

class InventoryViewSet(ModelViewSet):
 queryset = Inventory.objects.all()
 serializer_class = InventorySerializer
 pagination_class = CustomPagination

class EquipementsViewSet(ModelViewSet):
 queryset = Equipments.objects.all()
 serializer_class = EquipementsTSerializer
 pagination_class = CustomPagination