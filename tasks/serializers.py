from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Definicion del Serializer para el modelo task,
    se especifican sus campos a utilizar del modelo.
    """
    owner = serializers.ReadOnlyField(source="owner.email")  
    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "completed",
            "created",
            "owner"
        )


