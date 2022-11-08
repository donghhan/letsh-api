from rest_framework.serializers import ModelSerializer
from accomodations.serializers import *
from .models import *


class AllFavouritesSerializer(ModelSerializer):
    rooms = RoomListSerializer(many=True, read_only=True)

    class Meta:
        model = Favourites
        fields = ["pk", "name", "rooms"]
