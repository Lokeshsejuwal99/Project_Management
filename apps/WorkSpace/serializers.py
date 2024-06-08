from rest_framework.serializers import ModelSerializer
from apps.WorkSpace.models import WorkSpace


class WorkSpaceSerializer(ModelSerializer):
    class Meta:
        model = WorkSpace
        fields = '__all__'
