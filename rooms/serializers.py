from rest_framework import serializers
from .models import *
from users.serializers import *
from categories.serializers import *


class RoomAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomAmenity
        fields = "__all__"


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    amenity = RoomAmenitySerializer(read_only=True)
    owner = RoomOwnerSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Room
        exclude = ["created_at", "updated_at"]
