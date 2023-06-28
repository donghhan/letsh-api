from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import User
from rooms.models import *


class RoomInline(admin.TabularInline):
    model = Room
    max_num = 10
    verbose_name = _("Room owning")
    verbose_name_plural = _("Rooms owning")
    can_delete = False
    show_change_link = True


@admin.register(User)
class UserAdmin(UserAdmin):
    empty_value_display = "None"
    list_display = (
        "username",
        "email",
        "get_full_name",
        "mobile_number",
        "sex",
        "is_active",
    )
    inlines = [
        RoomInline,
    ]
    list_filter = ("sex",)
    list_per_page = 50
