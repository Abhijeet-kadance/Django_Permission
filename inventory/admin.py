from django.contrib import admin
from .models import Product
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def get_form(self,request,obj=None, **kwargs):
        form = super().get_form(request,obj,**kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True
            form.base_fields['is_superuser'].disabled = True
            form.base_fields['user_permissions'].disabled = True
            form.base_fields['groups'].disabled = True
        return form


# class ReadOnlyAdminMixin:
#     def has_add_permission(self, request):
#         return False
    
#     def has_change_permission(self, request, obj=None):
#         if request.user.has_perm('inventory.change_product'):
#             return False
#         else:
#             return False
    
#     def has_delete_permission(self, request, obj=None):
#         return False
        
#     def has_view_permission(self, request, obj=None):
#         return True

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ("name",)

    # def get_form(self,request,obj=None, **kwargs):
    #     form = super().get_form(request,obj,**kwargs)
    #     is_superuser = request.user.is_superuser

    #     if not is_superuser:
    #         form.base_fields['name'].disabled = True
    #     return form
    
    
    

# class MyAuthenticationBackend:

#     def authenticate(self, *args, **kwargs):
#         pass
    
#     def get_user(self, user_id):
#         try:
#             return get_user_model().objects.get(pk=user_id)
#         except get_user_model().DoesNotExist:
#             return None

#     def has_perm(self, user_obj, perm, obj=None):
#         if perm == "view_category":
#             return True # everybody can view
#         # otherwise only the owner or the superuser can delete
#         return user_obj.is_active and obj.user.pk==user_obj.pk

#     def has_perms(self, user_obj, perm_list, obj=None):
#         return all(self.has_perm(user_obj, perm, obj) for perm in perm_list)