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
    ]
    list_filter = ("room_type", "wifi")
    search_fields = ("name",)
    search_help_text = _("Searchable by name of accomodation.")


@admin.register(RoomAmenity)
class RoomAmenityAdmin(admin.ModelAdmin):
    list_display = ("name",)
