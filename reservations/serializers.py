from django.utils import timezone
from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            "reservation_id",
            "check_in",
            "check_out",
            "adult",
            "children",
            "room",
            "guest",
            "created_at",
        ]


class CreateReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            "check_in",
            "check_out",
            "guest",
            "adult",
            "children",
        ]

    def validate_check_in(self, attrs):
        now = timezone.localtime(timezone.now()).date()
        if now > attrs:
            raise serializers.ValidationError("Can't book in the past")
        return attrs

    def validate_check_out(self, attrs):
        now = timezone.localtime(timezone.now()).date()
        if now > attrs:
            raise serializers.ValidationError("Can't book in the past")
        return attrs

    def validate(self, attrs):
        # Check if check-out date is always later than check-in date
        if attrs["check_out"] <= attrs["check_in"]:
            raise serializers.ValidationError(
                "Check-out date should be less than check-in date."
            )

        # Checking duplicate reservations
        if Reservation.objects.filter(
            check_in__lt=attrs["check_out"], check_out__gt=attrs["check_in"]
        ).exists():
            raise serializers.ValidationError(
                "You cannot book accomodations on that period."
            )
        return super().validate(attrs)
