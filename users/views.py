from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from .serializers import *


class MyProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = PrivateUserSerializer(user).data
        return Response(serializer)

    def put(self, request):
        user = request.user
        serializer = PrivateUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            updated_profile_user = serializer.save()
            serializer = PrivateUserSerializer(updated_profile_user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserView(APIView):
    def post(self, request):
        # Validating password
        password = request.data.get("password")
        if not password:
            raise ParseError(_("You should provide a valid password."))
        serializer = PrivateUserSerializer(data=request.data)

        if serializer.is_valid():
            new_user = serializer.save()
            new_user.set_password(password)
            new_user.save()
            serializer = PrivateUserSerializer(new_user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PublicUserView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = PrivateUserSerializer(user)
        return Response(serializer.data)


class ChangePasswordView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password or not new_password:
            raise ParseError("Either old password or new password should be provided.")

        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            raise ParseError

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return Response({"ok": "Loggged in!"})
        else:
            return Response({"error": "wrong password"})


class LogoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok": "Logged out!"})
