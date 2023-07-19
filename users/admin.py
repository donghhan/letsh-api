from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from rooms.models import *


class RoomInline(admin.TabularInline):
    model = Room
    max_num = 10
    verbose_name = _("Room owning")
    verbose_name_plural = _("Rooms owning")
    can_delete = False
    show_change_link = True


class UserAdmin(BaseUserAdmin):
    empty_value_display = "None"
    list_display = (
        "username",
        "email",
        "get_full_name",
        "mobile_number",
        "sex",
        "is_active",
        "is_owner",
    )
    inlines = [
        RoomInline,
    ]
    fieldsets = [
        (
            "Personal Information",
            {
                "fields": [
                    "username",
                    "password",
                    "first_name",
                    "last_name",
                    "email",
                    "is_owner",
                    "date_joined",
                ],
                "classes": "wide",
            },
        ),
        (
            "Permission",
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ]
            },
        ),
    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    list_filter = ("sex", "is_owner")
    list_per_page = 50


admin.site.register(User, UserAdmin)
