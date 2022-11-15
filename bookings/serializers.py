from django.utils import timezone
from rest_framework.serializers import ModelSerializer, DateField, ValidationError
from .models import *


class CreateRoomBookingSerializer(ModelSerializer):
    check_in = DateField()
    check_out = DateField()

    class Meta:
        model = Booking
        fields = ["check_in", "check_out", "guests"]

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise ValidationError("Cannot book in the past")
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise ValidationError("Cannot checkout the past")
        return value

    def validate(self, data):
        if data["check_out"] <= data["check_in"]:
            raise ValidationError(
                "Check in date should be earlier than check out time."
            )

        existing_bookings = Booking.objects.filter(
            check_in__lte=data["check_out"], check_out__gte=data["check_in"]
        ).exists()
        if existing_bookings:
            raise ValidationError("Selected time already booked by others.")
        return data


class PublicBookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ["pk", "check_in", "check_out", "guests"]


class PrivateBookingSerializer(ModelSerializer):
    pass
