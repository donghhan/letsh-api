from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "get_total_room_by_categories")
