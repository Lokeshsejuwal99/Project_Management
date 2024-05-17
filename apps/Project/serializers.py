from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.Project.models import (
    Project,
    ProjectTag,
    MileStone,
    Dependencies,
    File,
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
    class Meta:
        model = Project
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class FileListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    one_file = serializers.ListField(child=serializers.FileField())

    def create(self, validated_data):
        name = validated_data['name']
        files_data = validated_data['one_file']
        for file_data in files_data:
            File.objects.create(Name=name, One_file=file_data)
        return validated_data