from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(RoomPhoto)
class RoomPhotoAdmin(admin.ModelAdmin):
    empty_value_dsipaly = "-----"
    list_display = (
        "room",
        "thumbnail",
        "preview_thumbnail",
        "photo",
    )
    readonly_fields = ("thumbnail",)

    def preview_thumbnail(self, obj):
        return format_html(f'<img src="{obj.thumbnail}" alt="{obj.room.name}" />')
