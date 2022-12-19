from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *
from users.serializers import *
from categories.serializers import *
from reviews.serializers import *
from user_media.serializers import *
from favourites.models import *


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        exclude = ["description"]


class RoomListSerializer(ModelSerializer):
    rating = SerializerMethodField()
    is_owner = SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = [
            "id",
            "name",
            "price_per_night",
            "is_free_breakfast",
            "is_free_internet",
            "is_free_parking",
            "is_free_booking_cancelation",
            "number_of_beds",
            "number_of_bedrooms",
            "number_of_bathrooms",
            "rating",
            "maximum_guests",
            "is_owner",
            "photos",
        ]

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user


class RoomDetailSerializer(ModelSerializer):
    owner = SimpleUserForOneRoomSerializer(read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = SerializerMethodField()
    is_owner = SerializerMethodField()
    is_liked = SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user

    def get_is_liked(self, room):
        request = self.context["request"]

        if request.user.is_authenticated:
            return Favourites.objects.filter(
                user=request.user, rooms__pk=room.pk
            ).exists()
