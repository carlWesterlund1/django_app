from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        print('permissions method running')
        user = request.user
        print(user.get_all_permissions())
        if user.is_staff:
            if user.has_perm("articles.add_article"):
                return True
            if user.has_perm("articles.delete_article"):
                return True
            if user.has_perm("articles.change_article"):
                return True
            if user.has_perm("articles.view_article"):
                return True
            return False
        return False 
