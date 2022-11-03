from rest_framework.serializers import ModelSerializer
from .models import *
from users.serializers import *
from categories.serializers import *


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        exclude = ["description"]


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "name",
            "price_per_night",
            "is_free_breakfast",
            "is_free_internet",
            "is_free_parking",
            "is_free_booking_cancelation",
            "number_of_beds",
            "number_of_bedrooms",
            "number_of_bathrooms",
            "maximum_guests",
        ]


class RoomDetailSerializer(ModelSerializer):
    owner = SimpleUserForOneRoomSerializer()  # Serializer won't ask owner
    amenities = AmenitySerializer(many=True)

    class Meta:
        model = Room
        fields = "__all__"
