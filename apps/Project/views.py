from rest_framework.viewsets import ModelViewSet
from Project_main.pagination import CustomPagination
from apps.Project.models import Project, ProjectTag, MileStone
from apps.Project.serializers import ProjectSerializer, ProjectTagSerializer, MileStoneSerializer
from Resource.nats_publisher import publish_inventory_created_event  # Import the function to publish events to NATS

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
 
