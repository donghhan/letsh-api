from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_200_OK
from .models import *
from .serializers import *
from accomodations.models import *


class AllFavouritesView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_favourites = Favourites.objects.filter(user=request.user)
        serializer = AllFavouritesSerializer(
            all_favourites, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = AllFavouritesSerializer(data=request.data)

        if serializer.is_valid():
            favourite = serializer.save(user=request.user)
            serializer = AllFavouritesSerializer(favourite)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class FavouriteDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Favourites.objects.get(pk=pk, user=user)
        except Favourites.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        favourite = self.get_object(pk, request.user)
        serializer = AllFavouritesSerializer(favourite)
        return Response(serializer.data)

    def put(self, request, pk):
        favourite = self.get_object(pk, request.user)
        serializer = AllFavouritesSerializer(favourite, data=request.data, partial=True)

        if serializer.is_valid():
            updated_favourite = serializer.save()
            serializer = AllFavouritesSerializer(updated_favourite)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        favourite = self.get_object(pk, request.user)
        favourite.delete()
        return Response(status=HTTP_200_OK)


class FavouriteToggle(APIView):
    def get_favourites(self, pk, user):
        try:
            return Favourites.objects.get(pk=pk, user=user)
        except Favourites.DoesNotExist:
            raise NotFound

    def get_room(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def put(self, request, pk, room_pk):
        favourite = self.get_list(pk, request.user)
        room = self.get_room(room_pk)

        if favourite.rooms.filter(pk=room_pk).exists():
            favourite.rooms.remove(room)
        else:
            favourite.rooms.add(room)
        return Response(status=HTTP_200_OK)
