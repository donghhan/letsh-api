from rest_framework.serializers import ModelSerializer
from .models import *


class SimpleUserForOneRoomSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["nickname", "profile_photo"]


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "is_active", "is_admin", "id"]
