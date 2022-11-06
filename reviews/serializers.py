from rest_framework.serializers import ModelSerializer
from .models import *
from users.serializers import *


class ReviewSerializer(ModelSerializer):

    user = SimpleUserForOneRoomSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["user", "review"]
