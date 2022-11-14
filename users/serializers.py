from rest_framework.serializers import ModelSerializer
from .models import *


class SimpleUserForOneRoomSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["nickname", "profile_photo"]
