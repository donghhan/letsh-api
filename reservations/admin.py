from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    empty_value_display = "-----"
    list_display = [
        "reservation_id",
        "get_guest_full_name",
        "get_guest_mobile_phone",
        "get_guest_email",
        "room",
        "check_in",
        "check_out",
        "adult",
        "children",
    ]
    readonly_fields = [
        "reservation_id",
        "reservation_created_time",
        "room",
        "get_total_stay_length",
    ]
    fieldsets = [
        (
            None,
            {
                "fields": ["reservation_id", "reservation_created_time"],
                "classes": ["wide"],
            },
        ),
        (
            "Guest Information",
            {
                "fields": ["guest", "adult", "children"],
            },
        ),
        (
            "Room Information",
            {
                "fields": ["room"],
            },
        ),
        (
            "Reservation Time",
            {
                "fields": ["check_in", "check_out", "get_total_stay_length"],
            },
        ),
    ]

    @admin.display(description="Reservation Created Time")
    def reservation_created_time(self, obj):
        return obj.created_at

    def get_guest_full_name(self, obj):
        full_name = obj.guest.get_full_name
        return full_name

    get_guest_full_name.short_description = "Name"

    def get_guest_mobile_phone(self, obj):
        mobile_number = obj.guest.mobile_number
        return mobile_number

    get_guest_mobile_phone.short_description = "Mobile Number"

    def get_guest_email(self, obj):
        email = obj.guest.email
        return email

    get_guest_email.short_description = "Email"

    def get_total_stay_length(self, obj):
        check_in = obj.check_in
        check_out = obj.check_out
        total_stay_length = (check_out - check_in).days
        return f"{total_stay_length} " + _("days")

    get_total_stay_length.short_description = "Total Staying Length"
