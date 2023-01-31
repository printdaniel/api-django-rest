from .models import Project 
from rest_framework import viewsets, permissions
from .serializer import ProjectSerializar

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializar
