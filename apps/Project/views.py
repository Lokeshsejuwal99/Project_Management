from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from Project_main.pagination import CustomPagination
from apps.Project.models import Project, ProjectTag, MileStone
from apps.Resource.models import  Employee_assigned, Inventory, Equipments
from apps.Project.serializers import ProjectSerializer, ProjectTagSerializer, MileStoneSerializer, InventorySerializer, EmployeesSerializer, EquipementsTSerializer

# Create your views here.

# Changeable Viewsets/Only for testing purposes
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

class ProjectTagViewSet(ModelViewSet):
 queryset = ProjectTag.objects.all()
 serializer_class = ProjectTagSerializer
 pagination_class = CustomPagination

class ProjectViewSet(ModelViewSet):
 queryset = Project.objects.all()
 serializer_class = ProjectSerializer
 pagination_class = CustomPagination

class MileStoneViewSet(ModelViewSet):
 queryset = MileStone.objects.all()
 serializer_class = MileStoneSerializer
 pagination_class = CustomPagination
 
