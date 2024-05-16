from django.shortcuts import render
from .models import Employee_assigned, Inventory, Equipments, Budget
from .serializers import InventorySerializer, EmployeesSerializer, EquipementsTSerializer, BudgetSerializer
from rest_framework.viewsets import ModelViewSet
from Project_main.pagination import CustomPagination
from rest_framework.response import Response
from rest_framework import status
from .publisher import publish_inventory_created_event
import asyncio

# Create your views here.


class EmployeeViewSet(ModelViewSet):
    queryset = Employee_assigned.objects.all()
    serializer_class = EmployeesSerializer
    pagination_class = CustomPagination


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            # Trigger event after successfully creating the inventory item
            asyncio.run(publish_inventory_created_event(request.data))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EquipementsViewSet(ModelViewSet):
    queryset = Equipments.objects.all()
    serializer_class = EquipementsTSerializer
    pagination_class = CustomPagination
    

class BudgetViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer