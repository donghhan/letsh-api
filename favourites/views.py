from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class AllFavouritesView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self):
        pass

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
