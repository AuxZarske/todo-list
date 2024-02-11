from rest_framework import permissions

class IsUnauthenticatedOrStaffOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permite el acceso si el usuario está desautenticado o es un staff o admin
        return not request.user.is_authenticated or request.user.is_staff or request.user.is_admin
