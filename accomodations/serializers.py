from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *
from users.serializers import *
from categories.serializers import *


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        exclude = ["description"]


class RoomListSerializer(ModelSerializer):
    rating = SerializerMethodField()
    is_owner = SerializerMethodField()

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
            "rating",
            "is_owner",
        ]

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user


class RoomDetailSerializer(ModelSerializer):
    owner = SimpleUserForOneRoomSerializer()  # Serializer won't ask owner
    amenities = AmenitySerializer(many=True)
    rating = SerializerMethodField()
    is_owner = SerializerMethodField()

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user

    class Meta:
        model = Room
        fields = "__all__"
