from django.shortcuts import get_object_or_404
from rest_framework import views
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from rest_framework.status import HTTP_200_OK
from .serializers import RoomAmenitySerializer, RoomSerializer
from .models import Room, RoomAmenity
from common.permissions import IsAdminOrReadOnly
from categories.models import Category


class RoomView(views.APIView):
    # Get all room information
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomSerializer(all_rooms, many=True)
        return Response(serializer.data)

    # Create new room
    def post(self, request):
        if request.user.is_authenticated:
            serializer = RoomSerializer(data=request.data)

            if serializer.is_valid():
                category_pk = request.data.get("category")
                try:
                    category = Category.objects.get(pk=category_pk)
                except Category.DoesNotExist:
                    raise ParseError("That category doesn't exist.")

                new_room = serializer.save(owner=request.user, category=category)

                # Amenities adding for room
                amenities = request.data.get("amenities")

                valid_amenities = []

                for amenity_pk in amenities:
                    amenity_to_include = get_object_or_404(RoomAmenity, pk=amenity_pk)
                    valid_amenities.append(amenity_to_include)

                new_room.amenities.set(valid_amenities)

                serializer = RoomSerializer(new_room)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class RoomDetailView(views.APIView):
    def get_object(self, pk):
        try:
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def put(self, request, pk):
        room = self.get_object(pk)

        if room.owner != request.user:
            raise PermissionDenied

        if request.user.is_authenticated:
            serializer = RoomSerializer(room, data=request.data, partial=True)

            if serializer.is_valid():
                category_pk = request.data.get("category")
                room_to_update = serializer.save()
                return Response(RoomSerializer(room_to_update).data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated

    def delete(self, request, pk):
        room = self.get_object(pk)

        if not request.user.is_authenticated:
            raise NotAuthenticated

        if room.owner != request.user:
            raise PermissionDenied

        room.delete()
        return Response(status=HTTP_200_OK)


class RoomAmenityView(views.APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        all_amenities = RoomAmenity.objects.all()
        serializer = RoomAmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomAmenitySerializer(data=dir(request).data)

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
            raise NotFound

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
