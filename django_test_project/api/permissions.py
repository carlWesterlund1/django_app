from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {                                     # dict of permissions for different actions
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)

    """def has_permission(self, request, view):
        print('permissions method running')
        user = request.user
        print(user.get_all_permissions())
        if user.is_staff:
            if user.has_perm("articles.add_article"): # "app_name.verb_model_name"
                return True
            if user.has_perm("articles.delete_article"):
                return True
            if user.has_perm("articles.change_article"):
                return True
            if user.has_perm("articles.view_article"):
                return True
            return False
        return False """


