from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied
from .serializers import *
from .models import *


class PhotoDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

    def delete(self, request, pk):
        photo = self.get_object(pk)

        if photo.room and photo.room.owner != request.user:
            raise PermissionDenied

        photo.delete()
        return Response(status=HTTP_200_OK)
