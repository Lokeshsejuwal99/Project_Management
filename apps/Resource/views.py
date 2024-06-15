from django.shortcuts import render
from .models import Employee_assigned, Inventory, Equipments, Budget
from .serializers import InventorySerializer, EmployeesSerializer, EquipementsTSerializer, BudgetSerializer
from rest_framework.viewsets import ModelViewSet
from Project_main.pagination import CustomPagination
from rest_framework.response import Response
from rest_framework import status
import asyncio
from apps.Resource.publisher import publish_inventory_created, publish_inventory_deleted, publish_inventory_updated

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
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        inventory_data = serializer.data

        try:
            asyncio.run(publish_inventory_created(inventory_data))
        except Exception as e:
            print(f'Error publishing inventory created event: {e}')

        response_data = {
            'message' : 'Inventory Created successfully.',
            'data' : serializer.data,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        inventory_data = serializer.data
        try:
            asyncio.run(publish_inventory_updated(inventory_data))
        except Exception as e:
            print(f'Error: Error occured while updating inventory. {e}')
        
        return Response(
            {
                'message' : 'Inventory updated successfully. ',
                'data' : serializer.data
            }
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        inventory_data = {
            # 'id': instance.id,
            # 'name': instance.Name,
        }
        try:
            asyncio.run(publish_inventory_deleted(inventory_data))
        except Exception as e:
            print(f'Error: Error while deleting inventory data: {e}')
        return Response('Inventory data is deleted.', status=status.HTTP_204_NO_CONTENT)
    

class EquipementsViewSet(ModelViewSet):
    queryset = Equipments.objects.all()
    serializer_class = EquipementsTSerializer
    pagination_class = CustomPagination
    

class BudgetViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer