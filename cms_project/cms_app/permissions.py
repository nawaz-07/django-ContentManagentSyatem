from rest_framework import permissions

class IsAdminOrAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is an admin or the content's author
        if request.user.is_admin or (view.kwargs.get('pk') and request.user == view.get_object().author):
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin or the content's author
        return request.user.is_staff or request.user == obj.author
