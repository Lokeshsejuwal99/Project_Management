from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from Project_main.pagination import CustomPagination
from apps.Project.models import Project, ProjectTag, MileStone
from apps.Project.serializers import ProjectSerializer, ProjectTagSerializer, MileStoneSerializer

# Create your views here.

# Changeable Viewsets/Only for testing purposes

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
 
