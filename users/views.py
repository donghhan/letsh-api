from rest_framework import views, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError
from .models import User
from .serializers import *


class MyProfileView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = PrivateMyProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = PrivateMyProfileSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            updated_user = serializer.save()
            serializer = PrivateMyProfileSerializer(updated_user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserView(views.APIView):
    def post(self, request):
        password = request.data.get("password")

        if not password:
            raise ParseError("Password is required.")

        serializer = PrivateMyProfileSerializer(data=request.data)

        if serializer.is_valid():
            new_user = serializer.save()
            new_user.set_password(password)
            new_user.save()
            serializer = PrivateMyProfileSerializer(new_user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
