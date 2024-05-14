from rest_framework.serializers import ModelSerializer
from apps.Project.models import Project, ProjectTag, MileStone, Dependencies, UploadedFile


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
        fields = '__all__'


class ProjectSerializer(ModelSerializer):
    files = FileSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = '__all__'
