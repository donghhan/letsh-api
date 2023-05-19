from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin
from .models import User


@register(User)
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
    list_filter = ("sex",)
    list_per_page = 50
