from rest_framework import views
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_200_OK
from .serializers import *
from .models import *


class RoomView(views.APIView):
    def get(self, request):
        """
        Get all room information
        """
        all_rooms = Room.objects.all()
        serializer = RoomSerializer(all_rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create new room
        """


class RoomDetailView(views.APIView):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass


class RoomAmenityView(views.APIView):
    def get(self, request):
        all_amenities = RoomAmenity.objects.all()
        serializer = RoomAmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomAmenitySerializer(data=request.data)

        if serializer.is_valid():
            new_amenity = serializer.save()
            return Response(RoomAmenitySerializer(new_amenity).data)


class RoomAmenityDetailView(views.APIView):
    def get_object(self, pk):
        try:
            amenity = RoomAmenity.objects.get(pk=pk)
            return amenity
        except RoomAmenity.DoesNotExist:
            return NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = RoomAmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = RoomAmenitySerializer(amenity, data=request.data, partial=True)

        if serializer.is_valid():
            amenity_to_update = serializer.save()
            return Response(RoomAmenitySerializer(amenity_to_update).data)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_200_OK)
