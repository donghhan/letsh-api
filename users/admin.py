from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    """User Admin Definition"""

    list_display = ("first_name", "last_name")
