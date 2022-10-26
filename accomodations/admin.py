from django.contrib import admin
from .models import *


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    """Amenity Admin Definition"""

    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    list_display = ("name", "price_per_night")
