from rest_framework.serializers import ModelSerializer
from apps.Task.models import Task, SubTask
from rest_framework import serializers

class SubTaskSerializer(ModelSerializer):
    class Meta: 
        model = SubTask
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)
    dependencies = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Task
        fields = '__all__'

