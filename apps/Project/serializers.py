from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.Project.models import (
    Project,
    ProjectTag,
    MileStone,
    Dependencies,
    ProjectFile,
)


class ProjectTagSerializer(ModelSerializer):
    class Meta:
        model = ProjectTag
        fields = "__all__"


class MileStoneSerializer(ModelSerializer):
    class Meta:
        model = MileStone
        fields = "__all__"


class DependenciesSerializer(ModelSerializer):
    class Meta:
        model = Dependencies
        fields = "__all__"


class ProjectSerializer(ModelSerializer):
    project_files = serializers.ListField(child=serializers.FileField(), allow_null=True, required=False)

    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        file_data = validated_data.pop('project_files', None)
        for Filedata in file_data:
            ProjectFile.objects.create(project=1, file=Filedata)
        inventory_data = validated_data.pop("Inventory", [])
        equipments_data = validated_data.pop("Equipments", [])
        assigned_members_data = validated_data.pop("Assigned_members", [])
        milestones_data = validated_data.pop("Milestones", [])
        dependencies_data = validated_data.pop("Dependencies", [])

        project = Project.objects.create(**validated_data)
        project.Inventory.set(inventory_data)
        project.Equipments.set(equipments_data)
        project.Assigned_members.set(assigned_members_data)
        project.Milestones.set(milestones_data)
        project.Dependencies.set(dependencies_data)

        return project
    
    def update(self, instance, validated_data):
        project_files_data = validated_data.pop("project_files", [])
        inventory_data = validated_data.pop("Inventory", [])
        equipments_data = validated_data.pop("Equipments", [])
        assigned_members_data = validated_data.pop("Assigned_members", [])
        milestones_data = validated_data.pop("Milestones", [])
        dependencies_data = validated_data.pop("Dependencies", [])

        instance.Name = validated_data.get("Name", instance.Name)
        instance.Description = validated_data.get("Description", instance.Description)
        instance.Start_date = validated_data.get("Start_date", instance.Start_date)
        instance.End_date = validated_data.get("End_date", instance.End_date)
        instance.Priority = validated_data.get("Priority", instance.Priority)
        instance.Status = validated_data.get("Status", instance.Status)
        instance.Last_updated = validated_data.get("Last_updated", instance.Last_updated)
        instance.Start_date = validated_data.get("Start_date", instance.Start_date)
        instance.Inventory.set(inventory_data)
        instance.Equipments.set(equipments_data)
        instance.Assigned_members.set(assigned_members_data)
        instance.Milestones.set(milestones_data)
        instance.Dependencies.set(dependencies_data)
        instance.save()

        # clear existing files and create new one
        instance.project_files.all().delete()
        for file_data in project_files_data:
            ProjectFile.objects.create(project=instance, **file_data)
        return instance
