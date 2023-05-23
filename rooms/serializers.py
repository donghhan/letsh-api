from rest_framework import serializers
from .models import *
from users.serializers import *


class RoomAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomAmenity
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    amenity = RoomAmenitySerializer()
    owner = RoomOwnerSerializer()

    class Meta:
        model = Room
        exclude = ["created_at", "updated_at"]
