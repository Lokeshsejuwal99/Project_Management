from rest_framework.viewsets import ModelViewSet
# from Project_main.pagination import CustomPagination
from apps.Project.models import Project, ProjectTag, MileStone, Dependencies
from apps.Project.serializers import ProjectSerializer, ProjectTagSerializer, MileStoneSerializer, DependenciesSerializer
from apps.Resource.publisher import publish_inventory_created_event
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import generics, parsers
from rest_framework.generics import CreateAPIView
from rest_framework.serializers import ModelSerializer

from rest_framework.parsers import MultiPartParser, FormParser

from .models import Project

from .serializers import ProductSerializer

# Create your views here.

# Changeable Viewsets/Only for testing purposes


class ProjectTagViewSet(ModelViewSet):
    queryset = ProjectTag.objects.order_by('name')
    serializer_class = ProjectTagSerializer
    # pagination_class = CustomPagination


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def perform_create(self, serializer):
        # Triggered when a new project is created
        instance = serializer.save()
        # Publish event to NATS when a new project is created
        publish_inventory_created_event(instance)

    def perform_update(self, serializer):
        # Triggered when a project is updated
        instance = serializer.save()
        # Publish event to NATS when a project is updated
        publish_inventory_created_event(instance)

    
class MileStoneViewSet(ModelViewSet):
    queryset = MileStone.objects.all()
    serializer_class = MileStoneSerializer
    # pagination_class = CustomPagination


class DependenciesViewSet(ModelViewSet):
    queryset = Dependencies.objects.all()
    serializer_class = DependenciesSerializer
    # pagination_class = CustomPagination


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # pagination_class = CustomPagination


# class FileUploadViewSet(generics.CreateAPIView):
#     parser_classes = [parsers.MultiPartParser, parsers.FormParser]
#     serializer_class = FileSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         Files = serializer.save()
#         return Response(FileSerializer(Files).data)

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()

    serializer_class = ProductSerializer


    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data, many=True)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)