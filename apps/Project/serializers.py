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


class FileListSerializer(serializers.Serializer) :
    name = serializers.CharField(max_length=50)
    one_file = serializers.ListField(
                       child=serializers.FileField( max_length=100000,
                                         allow_empty_file=False,
                                         use_url=False )
                                )
    
    def create(self, validated_data):
        name=validated_data.pop('name')
        one_file=validated_data.pop('one_file')
        for file in one_file:
            f = File.objects.create(name=name, one_file=file,**validated_data)
        return f


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File  
        fields = '__all__'