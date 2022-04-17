from rest_framework import permissions

WHITE_LIST_IPS = {
    "127.0.0.1": True
}


class BlocklistPermission(permissions.BasePermission):
    """
    Permission check for allow IPs.
    """

    def has_permission(self, request, view):
        _request_origin = request.headers.get("OriginUrl")
        return WHITE_LIST_IPS.get(_request_origin, False)
