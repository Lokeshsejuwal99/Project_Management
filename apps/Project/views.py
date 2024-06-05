from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from Project_main.pagination import CustomPagination
from apps.Task.models import Task, SubTask
from apps.Project.models import Project, ProjectTag, MileStone, Dependencies, WorkSpace
from apps.Task.serializers import TaskSerializer, SubTaskSerializer
from apps.Project.serializers import ProjectSerializer, ProjectTagSerializer, MileStoneSerializer, DependenciesSerializer, WorkSpaceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

# Create your views here.

# Changeable Viewsets/Only for testing purposes


class WorkSpaceViewSet(ModelViewSet):
    queryset = WorkSpace.objects.all()
    serializer_class = WorkSpaceSerializer

class ProjectTagViewSet(ModelViewSet):
    queryset = ProjectTag.objects.order_by('Name')
    serializer_class = ProjectTagSerializer
    pagination_class = CustomPagination


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = CustomPagination
    

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
            "message" : "Object-created successfully",
            "data" : serializer.data,
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
            {"message": "Object-updated successfully", "data": serializer.data}
        )
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=201)


# class GanttChartViewSet(ModelViewSet):
#     projects = Project.objects.all()
#     tasks = Task.objects.all()
#     dependencies = Dependencies.objects.all()
#     milestones = MileStone.objects.all()


class GanttChartViewSet(APIView):
    def get(self, request):
        """
        Handles GET requests to retrieve combined data.

        Returns:
            Response object with serialized project data:
                - projects (list): A list of serialized project objects.
                - tasks (list): A list of serialized task objects.
                - subtasks (list): A list of serialized subtaks objects.
                - dependencies (list): A list of serialized dependency objects.
                - milestones (list): A list of serialized milestone objects.
        """

        projects = Project.objects.all()
        tasks = Task.objects.all()
        subtasks = SubTask.objects.all()
        dependencies = Dependencies.objects.all()
        milestones = MileStone.objects.all()

        # Serialize data using appropriate serializers
        project_serializer = ProjectSerializer(projects, many=True)
        task_serializer = TaskSerializer(tasks, many=True)
        subtasks_serializer = SubTaskSerializer(subtasks, many=True)
        dependency_serializer = DependenciesSerializer(dependencies, many=True)
        milestone_serializer = MileStoneSerializer(milestones, many=True)

        combined_data = {
            'projects': project_serializer.data,
            'tasks': task_serializer.data,
            'subtasks': subtasks_serializer.data,
            'dependencies': dependency_serializer.data,
            'milestones': milestone_serializer.data,
        }

        return Response(combined_data, status=status.HTTP_200_OK)