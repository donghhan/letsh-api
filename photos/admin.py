from django.contrib import admin
from .models import *


@admin.register(RoomTypeThumbnail)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("file",)
