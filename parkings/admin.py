from django.contrib import admin
from .models import *


@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):

    """Parking Admin Model Definition"""

    list_display = ("name", "maximum_capacity", "category")
