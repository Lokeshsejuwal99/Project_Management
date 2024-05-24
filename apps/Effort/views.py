from django.shortcuts import render
from apps.Effort.models import EffortCalculation
from apps.Effort.serializers import EffortCalculateSerializer
from rest_framework import viewsets
from Project_main.pagination import CustomPagination

# Create your views here.
class EffortCalculationViewSet(viewsets.ModelViewSet):
 queryset = EffortCalculation.objects.all()
 serializer_class = EffortCalculateSerializer
 pagination_class = CustomPagination