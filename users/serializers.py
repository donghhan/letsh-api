from rest_framework import serializers
from rest_framework.status import HTTP_409_CONFLICT
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


class CheckExistingUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]
