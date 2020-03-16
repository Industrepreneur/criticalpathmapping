from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    "Restrict user account access to the specific user."

    def has_object_permission(self, request, view, user):
        if request.user:
            return user == request.user
        return False

        # TODO: Allow access by company managers
