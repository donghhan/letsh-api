from rest_framework import viewsets, parsers
from .models import *
from .serializers import *


class RoomTypeViewset(viewsets.ModelViewSet):
    queryset = RoomTypeThumbnail.objects.all()
    serializer_class = RoomTypeThumbnailSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
