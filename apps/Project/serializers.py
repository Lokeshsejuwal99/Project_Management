from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.Project.models import Project, ProjectTag, MileStone

class ProjectTagSerializer(ModelSerializer):
    class Meta:
        model = ProjectTag
        fields = "__all__"

class MultipleEmployeeAssign(serializers.Field):
    def __init__(self, choices, **kwargs):
        self.choices = choices
        super().__init__(**kwargs)

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        if isinstance(data, list):
            for item in data:
                if item not in self.choices:
                    raise serializers.ValidationError(f"{item} is not a valid choice")
            return data
        else:
            raise serializers.ValidationError("Expected a list of choices")
        
class ProjectSerializer(ModelSerializer):
    Employees_list = MultipleEmployeeAssign(choices=[
        'lokesh', 
        'pragyo',
        'krish', 
        'sagar',
        'manish',
        'sisir'
    ])
    class Meta:
        model = Project
        fields = [
            "id",
            "project_tag",
            "Name",
            "Description",
            "Priority",
            "Status",
            "Employees_list",
            "Start_date",
            "End_date",
            "Last_updated",
        ]     
class MileStoneSerializer(ModelSerializer):
    class Meta:
        model = MileStone
        fields = "__all__"

