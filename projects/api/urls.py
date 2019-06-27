from django.urls import path
from projects.api.views import (ProjectDetailAPIView, ProjectListCreateAPIView)

urlpatterns =[
    path("projects/", ProjectListCreateAPIView.as_view(), name="project-list"),
    path("projects/<int:pk>/", ProjectDetailAPIView.as_view(), name="project-detail"), 

]
