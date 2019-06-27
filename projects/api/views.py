from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pdb
from rest_framework.generics import get_object_or_404
from projects.models import Project, User
from projects.api.serializers import ProjectSerializer, UserSerializer

class ProjectListCreateAPIView(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProjectDetailAPIView(APIView):
    def get_object(self, pk):
        project = get_object_or_404(Project, pk=pk)
        return project

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(Project, data=request.data)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
