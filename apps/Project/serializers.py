from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apps.Project.models import (
    Project,
    ProjectTag,
    MileStone,
    Dependencies,
    UploadedFile,
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


class FileSerializer(ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ["project", "files"]


class ProjectSerializer(ModelSerializer):
    File = serializers.SerializerMethodField()

    def get_photos(self, obj):
        File = UploadedFile.objects.filter(project=obj)
        return FileSerializer(File, many=True, read_only=False).data

    class Meta:
        model = Project
        fields = [
            "project_tag",
            "Name",
            "Description",
            "Start_date",
            "End_date",
            "Priority",
            "Inventory",
            "Equipments",
            "Assigned_members",
            "Status",
            "Last_updated",
            "Milestones",
            "Dependencies",
            "File",
        ]
