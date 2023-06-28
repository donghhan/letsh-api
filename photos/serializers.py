from rest_framework import serializers
from .models import *


class RoomPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = "__all__"
