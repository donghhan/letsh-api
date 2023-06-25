from django.contrib import admin
from .models import *


@admin.register(RoomPhoto)
class RoomPhotoAdmin(admin.ModelAdmin):
    list_display = ("photo", "room")
