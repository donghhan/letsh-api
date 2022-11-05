from rest_framework.serializers import ModelSerializer
from .models import *


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
