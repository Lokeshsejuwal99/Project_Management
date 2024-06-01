from rest_framework.serializers import ModelSerializer
from apps.Task.models import Task, SubTask


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class SubTaskSerializer(ModelSerializer):
    class Meta: 
        model = SubTask
        fields = '__all__'