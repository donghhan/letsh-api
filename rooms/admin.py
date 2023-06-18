from django.contrib import admin
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
    )


@admin.register(RoomAmenity)
class RoomAmenityAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
