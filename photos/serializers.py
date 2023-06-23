from rest_framework import serializers
from .models import *


class RoomTypeThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomTypeThumbnail
        fields = "__all__"
