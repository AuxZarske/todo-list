from .models import Task
from .serializers import TaskSerializer  
from .permissions import IsOwner 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.utils.dateparse import parse_date

class TaskViewSet(viewsets.ModelViewSet):
    """
    Definicion de la vista para tasks.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsOwner, IsAuthenticated]

    def get_queryset(self):
        """
        Se define la devolucion de las tareas que unicamente le pertenescan al propietario.
        En caso de una query en la request se devuelve las tareas filtradas por fecha y contenido.
        """
        query = self.request.GET.get('query') 
        date_str = self.request.GET.get('date')    
        user = self.request.user

        queryset = Task.objects.filter(owner=user)

        if date_str:
            date = parse_date(date_str)
            if date:
                queryset = queryset.filter(created__date=date)
                
        
        if query:
            queryset = queryset.filter(
                Q(description__icontains=query) |
                Q(title__icontains=query)
            )

        return queryset

    def perform_create(self, serializer):
        """
        Se define que en la creacion de una tarea se agrega como propietario al usuario actual.
        """
        serializer.save(owner=self.request.user)

