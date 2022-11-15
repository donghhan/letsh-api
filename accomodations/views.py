from django.db import transaction  # If any codes have errors, queries won't be created.
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_200_OK
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from .models import *
from .serializers import *
from reviews.serializers import *
from categories.models import Category
from user_media.serializers import *
from bookings.models import *
from bookings.serializers import *


class AmenitiesView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

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

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity_to_update = self.get_object(pk)
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
        return Response(status=HTTP_200_OK)


class RoomsView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(
            all_rooms, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomDetailSerializer(data=request.data)

        if serializer.is_valid():
            # Creating category first for creating new room
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError(
                    _("You must choose a valid category before creating your own room.")
                )
            try:
                category = Category.objects.get(pk=category_pk)
            except Category.DoesNotExist:
                raise ParseError(_("There is no such category."))

            try:
                with transaction.atomic():
                    room_to_create = serializer.save(
                        owner=request.user, category=category
                    )
                    # Adding amenities
                    amenities_list = request.data.get("amenities")
                    for amenity_pk in amenities_list:
                        amenity = Amenity.objects.get(pk=amenity_pk)
                        room_to_create.amenities.add(amenity)
                    serializer = RoomDetailSerializer(room_to_create)
                    return Response(serializer.data)
            except Exception:
                raise ParseError(_("There is no such amenity."))
        else:
            return Response(serializer.errors)


class AllRoomsInMapView(APIView):
    def get(self, requset):
        all_rooms = Room.objects.all()

    def post(self, request):
        pass


class RoomDetailView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

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
        room_to_update = self.get_object(pk)

        # Check if user is an owner
        if request.user != room_to_update.owner:
            raise PermissionDenied

        serializer = RoomDetailSerializer(
            room_to_update, data=request.data, partial=True
        )

        if serializer.is_valid():
            category_to_update_pk = request.data.get("category")
            try:
                category = Category.objects.get(pk=category_to_update_pk)
            except Category.DoesNotExist:
                raise ParseError(_("There is no such category."))

            try:
                with transaction.atomic():
                    updated_room = serializer.save(category=category)
                    # Adding amenities
                    amenities_list = request.data.get("amenities")
                    for amenity_pk in amenities_list:
                        amenity = Amenity.objects.get(pk=amenity_pk)
                        updated_room.amenities.add(amenity)
                    serializer = RoomDetailSerializer(updated_room)
                    return Response(serializer.data)
            except Exception:
                raise ParseError(_("There is no such amenity."))
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        room_to_delete = self.get_object(pk)

        # Check if user is logged in
        if not request.user.is_authenticated:
            raise NotAuthenticated
        # Check if user is an owner
        if request.user != room_to_delete.owner:
            raise PermissionDenied

        room_to_delete.delete()
        return Response(status=HTTP_200_OK)


class RoomReviewView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        # Pagination
        page_size = 5
        start = (page - 1) * page_size
        end = start + page_size

        room = self.get_object(pk)
        serializer = ReviewSerializer(room.reviews.all()[start:end], many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            review = serializer.save(user=request.user, room=self.get_object(pk))
            serializer = ReviewSerializer(review)
            return Response(serializer.data)


class RoomPhotoView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        room = self.get_object(pk)

        if request.user != room.owner:
            raise PermissionDenied

        serializer = PhotoSerializer(data=request.data)

        if serializer.is_valid():
            photo = serializer.save(room=room)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class RoomBookingView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        now = timezone.localtime(timezone.now())
        bookings = Booking.objects.filter(room=room, check_in__gt=now)
        serializer = PublicBookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        room = self.get_object(pk)
        serializer = CreateRoomBookingSerializer(data=request.data)

        if serializer.is_valid():
            new_booking = serializer.save(room=room, user=request.user)
            serializer = PublicBookingSerializer(new_booking)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
