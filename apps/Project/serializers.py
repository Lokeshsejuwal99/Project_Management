from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.Project.models import Project, ProjectTag, MileStone, Employee_assigned, Equipments, Inventory

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

class ProjectTagSerializer(ModelSerializer):
    class Meta:
        model = ProjectTag
        fields = "__all__"
        
class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class MileStoneSerializer(ModelSerializer):
    class Meta:
        model = MileStone
        fields = "__all__"

