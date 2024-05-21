from rest_framework.viewsets import ModelViewSet
from Project_main.pagination import CustomPagination
from apps.Project.models import Project, ProjectTag, MileStone, Dependencies
from apps.Project.serializers import ProjectSerializer, ProjectTagSerializer, MileStoneSerializer, DependenciesSerializer
from .models import Project
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
# Create your views here.

# Changeable Viewsets/Only for testing purposes


class ProjectTagViewSet(ModelViewSet):
    queryset = ProjectTag.objects.order_by('name')
    serializer_class = ProjectTagSerializer
    pagination_class = CustomPagination


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all().order_by('Name')
    serializer_class = ProjectSerializer
    pagination_class = CustomPagination
    
    # def perform_create(self, serializer):
    #     # Triggered when a new project is created
    #     instance = serializer.save()
    #     # Publish event to NATS when a new project is created
    #     publish_inventory_created_event(instance)

    # def perform_update(self, serializer):
    #     # Triggered when a project is updated
    #     instance = serializer.save()
    #     # Publish event to NATS when a project is updated
    #     publish_inventory_created_event(instance)

    
class MileStoneViewSet(ModelViewSet):
    queryset = MileStone.objects.all().order_by('Name')
    serializer_class = MileStoneSerializer
    pagination_class = CustomPagination


class DependenciesViewSet(ModelViewSet):
    queryset = Dependencies.objects.all()
    serializer_class = DependenciesSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend] 
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_data = {
            "message": "Object-created successfully", 
            "data": serializer.data,
        }
        return Response(response_data, status=201)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(
                {"message": "paginated-list", "data": serializer.data}
            )
        return Response({"message": "Projects-list", "data": serializer.data})
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {"message": "Object-retrieved successfully", "data": serializer.data}
        )
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Object-updated successfully", "data":serializer.data}
        )
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=201)

# class FilesAPIView(APIView):
#     parser_classes = (MultiPartParser, FormParser, JSONParser)

#     def get(self, request, *args, **kwargs):
#         files = File.objects.all()
#         serializer = FileSerializer(files, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request, *args, **kwargs):
#         serializer = FileListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Files uploaded successfully"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
# class FilesAPIViewDetail(APIView):

#     def get_object(self, pk):
#         try: 
#             return File.objects.get(pk=pk)
#         except File.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk, format=None):
#         file = self.get_object(pk)
#         serializer = FileSerializer(file)
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         file = self.get_object(pk)
#         serializer = FileSerializer(file, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         file = self.get_object(pk)
#         file.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)
    