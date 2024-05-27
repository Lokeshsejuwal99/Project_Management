from apps.Resource.models import Employee_assigned, Equipments, Inventory, Budget
from rest_framework.serializers import ModelSerializer


class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employee_assigned
        fields = '__all__'


class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class EquipementsTSerializer(ModelSerializer):
    class Meta:
        model = Equipments
        fields = "__all__"


class BudgetSerializer(ModelSerializer):
    class Meta:
        model = Budget
        fields = "__all__"