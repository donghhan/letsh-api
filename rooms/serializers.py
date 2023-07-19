from rest_framework import serializers
from .models import *
from reviews.models import *
from users.serializers import *
from categories.serializers import *


class RoomAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomAmenity
        fields = "__all__"


class RoomTypeSerializer(serializers.ModelSerializer):
    total_rooms = serializers.SerializerMethodField()

    def get_total_rooms(self, obj):
        return obj.total_rooms()

    class Meta:
        model = RoomType
        fields = "__all__"


class RoomAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomAddress
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    amenity = RoomAmenitySerializer(read_only=True)
    owner = RoomOwnerSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    room_type = RoomTypeSerializer(read_only=True)
    address = serializers.CharField(source="address.city", read_only=True)
    total_reviews = serializers.SerializerMethodField()
    average_total_rating = serializers.SerializerMethodField()

    def get_total_reviews(self, obj):
        return obj.total_reviews()

    def get_average_total_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            total_rating = sum([review.average_total_rating() for review in reviews])
            average_rating = total_rating / len(reviews)
            return round(average_rating, 2)
        return None

    class Meta:
        model = Room
        exclude = [
            "created_at",
            "updated_at",
        ]


class SimplifiedRoomSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = [
            "pk",
            "name",
            "price_per_night",
            "average_rating",
        ]

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            total_rating = sum([review.average_rating() for review in reviews])
            average_rating = total_rating / len(reviews)
            return round(average_rating, 2)
        return None


class RoomPhotoSerializer(serializers.ModelSerializer):
    pass
