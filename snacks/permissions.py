from rest_framework import permissions

class IsPurchaserOrReadOnly(permissions.BasePermission):
  def had_object_permission(self, request, view, obj):

    if request.method in permissions.SAFE_METHODS:

      return True

    if obj.purchaser is None:
      return True

    return obj.purchaser == request.user