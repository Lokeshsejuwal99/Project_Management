from rest_framework.viewsets import ModelViewSet
from Project_main.pagination import CustomPagination
from apps.Project.models import Project, ProjectTag, MileStone, Dependencies
from apps.Project.serializers import ProjectSerializer, ProjectTagSerializer, MileStoneSerializer, DependenciesSerializer
from apps.Resource.publisher import publish_inventory_created_event
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

# Changeable Viewsets/Only for testing purposes


class ProjectTagViewSet(ModelViewSet):
    queryset = ProjectTag.objects.order_by('name')
    serializer_class = ProjectTagSerializer
    pagination_class = CustomPagination


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = CustomPagination
    parser_classes = (MultiPartParser, FormParser)
    
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
