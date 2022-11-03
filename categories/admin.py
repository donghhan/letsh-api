from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    """Category Admin Definition"""

    list_display = ("name", "kind")
