from rest_framework.viewsets import ModelViewSet
from Project_main.pagination import CustomPagination
from apps.Task.serializers import TaskSerializer, SubTaskSerializer
from apps.Task.models import Task, SubTask

# Create your views here.


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = CustomPagination


class SubTaskViewSet(ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer