from rest_framework import views
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_200_OK
from .models import *
from .serializers import *


class CategoryView(views.APIView):
    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            new_category = serializer.save()
            return Response(CategorySerializer(new_category).data)
        else:
            return Response(serializer.errors)


class CategoryDetailView(views.APIView):
    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
            return category
        except Category.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)

        if serializer.is_valid():
            category_to_update = serializer.save()
            return Response(CategorySerializer(category_to_update).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=HTTP_200_OK)
