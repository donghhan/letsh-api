from django.db import transaction  # If any codes have errors, queries won't be created.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from .models import *
from .serializers import *
from categories.models import Category


class AllAmenitiesView(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            new_amenity = serializer.save()
            return Response(AmenitySerializer(new_amenity).data)
        else:
            return Response(serializer.errors)


class AmenityDetailView(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = Amenity.objects.get(pk=pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity_to_update = Amenity.objects.get(pk=pk)
        serializer = AmenitySerializer(
            amenity_to_update, data=request.data, partial=True
        )
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity_to_delete = self.get_object(pk)
        amenity_to_delete.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class AllRoomsView(APIView):
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(
            all_rooms, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = RoomDetailSerializer(data=request.data)

            if serializer.is_valid():
                # Grab that category through request.data
                category_pk = request.data.get("category")
                if not category_pk:
                    raise ParseError("Category is not found.")
                # Search that category from DB
                try:
                    category = Category.objects.get(pk=category_pk)
                    # Throw error if user tries to connect accomodations with invalid categories (parking & mobile)
                    if (
                        category.kind == Category.CategoryKindChoices.PARKING
                        or category.kind == Category.CategoryKindChoices.MOBILE
                    ):
                        raise ParseError(
                            "Category should be neither parking nor mobile."
                        )
                except Category.DoesNotExist:
                    raise ParseError

                try:
                    with transaction.atomic():
                        new_room = serializer.save(
                            owner=request.user, category=category
                        )  # Send that category into serializer.save()

                        amenities = request.data.get("amenities")
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            new_room.amenities.add(amenity)
                        serializer = RoomDetailSerializer(new_room)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("There was something error for adding amenities.")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class AllRoomsInMapView(APIView):
    def get(self, requset):
        all_rooms = Room.objects.all()

    def post(self, request):
        pass


class RoomDetailView(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        if request.user.is_authenticated:
            room_to_update = Room.objects.get(pk=pk)
            serializer = RoomDetailSerializer(data=request.data)
        else:
            raise NotAuthenticated

    def delete(self, request, pk):
        room_to_delete = self.get_object(pk)

        # You cannot delete room if you're not logged in
        if not request.user.is_authenticated:
            raise NotAuthenticated
        # You cannot delete room if user is not an owner
        if room_to_delete.owner != request.user:
            raise PermissionDenied

        room_to_delete.delete()
        return Response(status=HTTP_204_NO_CONTENT)
