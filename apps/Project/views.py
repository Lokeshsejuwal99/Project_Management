from rest_framework.viewsets import ModelViewSet
from Project_main.pagination import CustomPagination
from apps.Project.models import Project, ProjectTag, MileStone, Dependencies, File
from apps.Project.serializers import ProjectSerializer, ProjectTagSerializer, MileStoneSerializer, DependenciesSerializer, FileListSerializer, FileSerializer
from apps.Resource.publisher import publish_inventory_created_event
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from .models import Project

# Create your views here.

# Changeable Viewsets/Only for testing purposes


class ProjectTagViewSet(ModelViewSet):
    queryset = ProjectTag.objects.order_by('name')
    serializer_class = ProjectTagSerializer
    pagination_class = CustomPagination


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
    pagination_class = CustomPagination


class DependenciesViewSet(ModelViewSet):
    queryset = Dependencies.objects.all()
    serializer_class = DependenciesSerializer
    pagination_class = CustomPagination


class FilesAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request, format=None, *args, **kwargs):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FileListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class FilesAPIViewDetail(APIView):

    def get_object(self, pk):
        try:
            return File.objects.get(pk=pk)
        except File.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = FileSerializer(file)  
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = FileSerializer(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        file = self.get_object(pk)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
