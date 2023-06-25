from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK
from .models import Category
from .serializers import CategorySerializer
from common.permissions import IsAdminOrReadOnly


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
