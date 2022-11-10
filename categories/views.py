from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
