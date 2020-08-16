from rest_framework.permissions import BasePermission

class CheckPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.method.lower() == 'get':
            return True
        return False
        