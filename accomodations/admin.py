from django.contrib import admin
from .models import *


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    """Amenity Admin Definition"""

    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    list_display = ("name", "room_category", "price_per_night", "owner")
    list_per_page = 50
    fieldsets = (
        (
            None,
            {"fields": ("name", "room_category", "price_per_night", "maximum_guests")},
        ),
        (
            "Freebies",
            {
                "classes": ("extrapretty",),
                "fields": (
                    "is_free_breakfast",
                    "is_free_internet",
                    "is_free_parking",
                    "is_free_booking_cancelation",
                ),
            },
        ),
        (
            "Facilities",
            {
                "classes": ("wide",),
                "fields": (
                    "number_of_beds",
                    "number_of_bedrooms",
                    "number_of_bathrooms",
                ),
            },
        ),
    )
