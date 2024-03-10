from django.contrib import admin
from django.contrib.auth.models import Group

from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_superuser")
    readonly_fields = ('created_at', 'updated_at')
    ordering = ("-updated_at",)
    exclude = ("username", )

    fieldsets = (
        (None, {"fields": ("username", "email", "first_name", "last_name",
                            "is_active", "created_at", "updated_at")}),
        ("Permissions", {"fields": ("is_superuser", "is_staff", "user_permissions")}),
    )

admin.site.register(CustomUser, UserAdmin)  # CustomUserモデルを登録
admin.site.unregister(Group)  # Groupモデルは不要のため非表示