from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Permiso personalizado para permitir unicamente al propietario de la tarea modificarla.
    """

    def has_object_permission(self, request, view, obj): 
        return obj.owner == request.user