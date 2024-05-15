from rest_framework.serializers import ModelSerializer
from apps.Task.models import Task, Employee_assigned_Task, Inventory_Task, Equipments_Task
from rest_framework import serializers


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
    Inventory = serializers.PrimaryKeyRelatedField(queryset=Inventory_Task.objects.all(), many=True)
    Equipments = serializers.PrimaryKeyRelatedField(queryset=Equipments_Task.objects.all(), many=True)
    class Meta:
        model = Task
        fields = '__all__'
