from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price_per_night",
        "room_type",
        "guest",
        "bedroom",
        "bathroom",
        "wifi",
        "owner",
        "total_reviews",
    )


@admin.register(RoomAmenity)
class RoomAmenityAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    empty_value_display = "None"
    list_display = (
        "name",
        "room_type_thumbnail_preview",
    )

    def room_type_thumbnail_preview(self, obj):
        if obj.cover_image:
            return format_html(
                f'<img src="{obj.cover_image.url}" style="width: 300px;" />'
            )
        else:
            return None
