from django.contrib import admin
from .models import *


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    """Amenity Admin Definition"""

    list_display = ("name", "description")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    @admin.action(description="Mark selected users as inactive")
    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active=False)

    list_display = ("name", "category", "price_per_night", "owner", "rating")
    list_per_page = 50
    empty_value_display = "(unknown)"
    search_fields = ("name",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "category",
                    "price_per_night",
                    "maximum_guests",
                    "owner",
                )
            },
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
    actions = [make_inactive]
