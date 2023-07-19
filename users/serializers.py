from rest_framework import serializers
from .models import *


class PrivateMyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "mobile_number",
            "sex",
            "is_owner",
            "profile_picture",
        ]


class RoomOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "is_owner",
        ]
