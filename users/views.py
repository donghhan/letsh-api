from django.contrib.auth import authenticate, login, logout
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


class ChangePasswordView(views.APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        confirm_new_password = request.data.get("confirm_new_password")

        if not old_password or not new_password or not confirm_new_password:
            raise ParseError("You should fill out all details.")

        if old_password == new_password:
            raise ParseError(
                "New password is too similar with old password. Try another one."
            )

        if new_password != confirm_new_password:
            raise ParseError("New password and confirm_password do not match.")

        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise ParseError("You should provide both username and password.")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response({"ok": "Successfully logged in"})
        else:
            return Response({"error": "Wrong password"})


class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok": "Logged out successfully"})
