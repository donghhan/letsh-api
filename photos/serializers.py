from rest_framework import serializers
from .models import *


class RoomTypeThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomTypeThumbnail
        fields = "__all__"


class RoomPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = "__all__"
