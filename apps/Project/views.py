from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.Project.models import Project, ProjectTag, MileStone, Employee_assigned, Inventory, Equipments
from apps.Project.serializers import ProjectSerializer, ProjectTagSerializer, MileStoneSerializer, InventorySerializer, EmployeesSerializer, EquipementsTSerializer

# Create your views here.

# Changeable Viewsets/Only for testing purposes
class EmployeeViewSet(ModelViewSet):
 queryset = Employee_assigned.objects.all()
 serializer_class = EmployeesSerializer

class InventoryViewSet(ModelViewSet):
 queryset = Inventory.objects.all()
 serializer_class = InventorySerializer

class EquipementsViewSet(ModelViewSet):
 queryset = Equipments.objects.all()
 serializer_class = EquipementsTSerializer

class ProjectTagViewSet(ModelViewSet):
 queryset = ProjectTag.objects.all()
 serializer_class = ProjectTagSerializer
 
class ProjectViewSet(ModelViewSet):
 queryset = Project.objects.all()
 serializer_class = ProjectSerializer

class MileStoneViewSet(ModelViewSet):
 queryset = MileStone.objects.all()
 serializer_class = MileStoneSerializer
 
