from rest_framework.serializers import ModelSerializer
from .models import *


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        exclude = ["caption"]
