from rest_framework.serializers import ModelSerializer
from apps.Task.models import Task, SubTask
from apps.Project.models import MileStone, Dependencies


class MilestoneSerializer(ModelSerializer):
    class Meta:
        model = MileStone
        fields = '__all__'


class DependenciesSerializer(ModelSerializer):
    class Meta:
        model = Dependencies
        fields = '__all__'
        ref_name = 'TaskAppDependencies'


class SubTaskSerializer(ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    subtask = SubTaskSerializer(many=True, read_only=True)
    milestones = MilestoneSerializer(many=True, read_only=True)
    dependencies = DependenciesSerializer(many=True, read_only=True)

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
            'milestones',
            'subtask']
