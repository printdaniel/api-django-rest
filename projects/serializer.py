from rest_framework import serializers
from .models import Project


class ProjectSerializar(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_filed = ('created_at',)



