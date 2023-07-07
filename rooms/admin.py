from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *
from users.models import *


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    empty_value_display = "-----"
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
        "category",
    )

    fieldsets = [
        (
            "Accomodation",
            {
                "fields": [
                    "name",
                    "price_per_night",
                    "room_type",
                    "guest",
                    "bedroom",
                    "bathroom",
                    "wifi",
                ],
                "classes": "wide",
            },
        ),
        (
            "Owner",
            {
                "fields": [
                    "owner",
                ]
            },
        ),
        (
            "Category",
            {
                "fields": [
                    "category",
                ]
            },
        ),
        (
            "Location",
            {
                "fields": [
                    "address",
                ]
            },
        ),
    ]
    list_filter = ("room_type", "wifi")
    search_fields = ("name",)
    search_help_text = _("Searchable by name of accomodation.")


@admin.register(RoomAmenity)
class RoomAmenityAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = (
        "room_type",
        "total_rooms",
    )


@admin.register(RoomAddress)
class RoomAddressAdmin(admin.ModelAdmin):
    empty_value_display = "-----"
    list_display = (
        "country",
        "city",
    )
    raw_id_fields = [
        "city",
    ]
