from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.WorkSpace.models import WorkSpace
from apps.WorkSpace.serializers import WorkSpaceSerializer
from Project_main.pagination import CustomPagination

# Create your views here.


class WorkSpaceViewSet(ModelViewSet):
    queryset = WorkSpace.objects.all()
    serializer_class = WorkSpaceSerializer
    pagination_class = CustomPagination
