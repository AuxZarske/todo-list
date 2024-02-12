from django.db import models
from django.conf import settings 


class Task(models.Model):
    """
    Se define el modelo Task para las tareas del usuario, se incluye la fecha en que es creada, el titulo
    su descripcion, el estado en que se encuentra, y el usuario que la creo.
    """
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=450, blank=True, default="")
    completed = models.BooleanField(default=False,blank=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="tasks", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.title