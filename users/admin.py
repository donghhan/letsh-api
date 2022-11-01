from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *


@admin.action(description="Convert activity of selected users.")
def set_activity(modeladmin, request, users):
    for user in users.all():
        if user.is_active == False:
            user.is_active = True
            user.save()
        else:
            user.is_active = False
            user.save()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    """User Admin Definition"""

    list_display = (
        "nickname",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "sex",
        "language",
        "currency",
        "is_host",
        "is_active",
    )
    list_filter = (
        "sex",
        "language",
        "currency",
        "is_host",
        "is_active",
    )
    list_per_page = 50
    radio_fields = {"sex": admin.HORIZONTAL}
    search_fields = ["nickname", "email", "phone_number"]
    search_help_text = "Searching avilable with nickname, email and phone number."
    fieldsets = (
        (
            "Personal Information",
            {
                "classes": "wide",
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "nickname",
                    "sex",
                    "phone_number",
                ),
            },
        ),
        (
            "Preference",
            {
                "classes": "wide",
                "fields": (
                    "language",
                    "currency",
                ),
            },
        ),
        (
            "Status",
            {
                "classes": ("collapse",),
                "fields": (
                    "is_host",
                    "is_active",
                    "is_admin",
                ),
            },
        ),
    )
    empty_value_display = "(unknown)"
    actions = [set_activity]
