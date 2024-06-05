from rest_framework.serializers import ModelSerializer
from apps.Task.models import Task, SubTask
from apps.Project.serializers import DependenciesSerializer


class SubTaskSerializer(ModelSerializer):
    class Meta: 
        model = SubTask
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    dependencies = DependenciesSerializer(many=True)
    
    class Meta:
        model = Task
        fields = [
            'Project',
            'Name',
            'Description',
            'Start_date',
            'End_date',
            'Priority',
            'Inventory',
            'Equipments',
            'Assigned_members',
            'Status',
            'Last_updated',
            'dependencies',
        ]