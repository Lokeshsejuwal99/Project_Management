from rest_framework.viewsets import ModelViewSet
from Project_main.pagination import CustomPagination
from apps.Project.models import Project, ProjectTag, MileStone, Dependencies, UploadedFile
from apps.Project.serializers import ProjectSerializer, ProjectTagSerializer, MileStoneSerializer, DependenciesSerializer, FileSerializer
from apps.Resource.publisher import publish_inventory_created_event
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
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


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        instance_data = request.data
        data = {key: value for key, value in instance_data.items()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if request.FILES:
            files = dict((request.FILES).lists()).get('files', None)
            if files:
                for file in files:
                    files_data = {}
                    files_data["blogs"] = instance.pk
                    files_data["image"] = files
                    files_serializer = FileSerializer(data=files_data)
                    files_serializer.is_valid(raise_exception=True)
                    files_serializer.save()

        return Response(serializer.data)

    # @action(detail=True, methods=['post'])
    # def upload_file(self, request, pk=None):
    #     project = self.get_object()
    #     file_serializer = FileSerializer(data=request.data)
    #     if file_serializer.is_valid():
    #         file_serializer.save(project=project)
    #         return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# class FileUploadView(APIView):
#     def post(self, request, format=None):
#         serializer = FileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class FileUploadView(ViewSet):
#     @action(detail=False, methods=['post'])
#     def upload(self, request):
#         serializer = FileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  