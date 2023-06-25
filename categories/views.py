from rest_framework import viewsets
from rest_framework import views
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Category
from rooms.models import Room
from .serializers import CategorySerializer
from rooms.serializers import SimplifiedRoomSerializer
from common.permissions import IsAdminOrReadOnly


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SimplifiedRoomByCategories(views.APIView):
    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
            return category
        except Category.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        category = self.get_object(pk=pk)
        all_rooms_by_category = Room.objects.filter(category=category)
        serializer = SimplifiedRoomSerializer(all_rooms_by_category, many=True)
        return Response(serializer.data)
