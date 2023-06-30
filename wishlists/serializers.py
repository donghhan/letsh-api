from rest_framework import serializers
from .models import *


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"
