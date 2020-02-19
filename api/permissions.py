# api/permissions.py
from rest_framework import permissions

class IsTweetAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS are: GET, OPTIONS, HEAD
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise, only the tweet author can change a tweet
        return obj.user == request.user
