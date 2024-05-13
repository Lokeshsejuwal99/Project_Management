from rest_framework.serializers import ModelSerializer
from apps.Project.models import Project, ProjectTag, MileStone, Dependencies


class ProjectTagSerializer(ModelSerializer):
    class Meta:
        model = ProjectTag
        fields = "__all__"


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class MileStoneSerializer(ModelSerializer):
    class Meta:
        model = MileStone
        fields = "__all__"


class DependenciesSerializer(ModelSerializer):
    class Meta:
        model = Dependencies
        fields = "__all__"