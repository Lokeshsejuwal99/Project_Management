from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apps.Project.models import (
    Project,
    ProjectTag,
    MileStone,
    Dependencies,
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


# class FileSerializer(ModelSerializer):
#     File = serializers.ListField(child=serializers.FileField())
#     class Meta:
#         model = UploadedFile
#         fields = ('files', 'File')

from rest_framework import serializers
from .models import Project, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)

    class Meta:
        model = ProductImage
        fields = ['project', 'images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop("images")
        product = Project.objects.create(**validated_data)

        for image in uploaded_images:
            ProductImage.objects.create(product=product, image=image)

        return product