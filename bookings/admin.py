from django.contrib import admin
from .models import *


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    """Booking Admin Model Definition"""

    list_display = ("user", "room", "check_in", "check_out", "guests")
