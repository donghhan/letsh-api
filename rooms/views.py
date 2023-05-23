from rest_framework import views
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_200_OK
from .serializers import *
from .models import *
from .permissions import *


class RoomView(views.APIView):
    permission_classes = [IsAdminOrReadOnly]

    # Get all room information
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomSerializer(all_rooms, many=True)
        return Response(serializer.data)

    # Create new room
    def post(self, request):
        serializer = RoomSerializer(data=request.data)

        if serializer.is_valid():
            new_room = serializer.save()
            return Response(RoomSerializer(new_room).data)


class RoomDetailView(views.APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, pk):
        try:
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist:
            return NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def put(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomSerializer(room, data=request.data, partia=True)

        if serializer.is_valid():
            room_to_update = serializer.save()
            return Response(RoomSerializer(room_to_update).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        room = self.get_object(pk)
        room.delete()
        return Response(status=HTTP_200_OK)


class RoomAmenityView(views.APIView):
    permission_classes = [IsAdminOrReadOnly]

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
    permission_classes = [IsAdminOrReadOnly]

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
