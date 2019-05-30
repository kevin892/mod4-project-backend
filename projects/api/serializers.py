from rest_framework import serializers
from projects.models import Project, User


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields ="__all__"

class UserSerializer(serializers.ModelSerializer):
    projects = serializers.HyperlinkedRelatedField(many=True,
                                                   read_only=True,
                                                   view_name="project-detail")
    class Meta:
        model = User
        fields = "__all__"
