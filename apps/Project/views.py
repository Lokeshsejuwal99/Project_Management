from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.Project.models import Project, ProjectTag, MileStone
from apps.Project.serializers import ProjectSerializer, ProjectTagSerializer, MileStoneSerializer

# Create your views here.

class ProjectTagViewSet(ModelViewSet):
 queryset = ProjectTag.objects.all()
 serializer_class = ProjectTagSerializer
 
class ProjectViewSet(ModelViewSet):
 queryset = Project.objects.all()
 serializer_class = ProjectSerializer

class MileStoneViewSet(ModelViewSet):
 queryset = MileStone.objects.all()
 serializer_class = MileStoneSerializer
 
