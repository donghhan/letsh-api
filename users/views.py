import requests
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework import views, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError, NotFound
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


class SignupView(views.APIView):
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


class LineLoginView(views.APIView):
    def post(self, request):
        code = request.data.get("code")
        # client_id = str(os.environ.get("LINE_OAUTH_CLIENT_ID"))
        # client_secret = str(os.environ.get("LINE_OAUTH_CLIENT_SECRET"))
        access_token = (
            requests.post(
                f"https://api.line.me/oauth2/v2.1/token?code={code}&client_id={settings.LINE_OAUTH_CLIENT_ID}&client_secret={settings.LINE_OAUTH_CLIENT_SECRET}&grant_type=authorization_code&redirect_uri=http://127.0.0.1:5173",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            .json()
            .get("access_token")
        )

        user_info = requests.get(
            f"https://api.line.me/oauth2/v2.1/userinfo",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/json",
            },
        ).json()


class CheckExistingUsernameView(views.APIView):
    def get(self, request):
        username = request.query_params.get("username", None)

        if not username:
            return Response(
                {"error": "Username parameter is missing"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(username=username)
            return Response({"usernameExists": True})
        except User.DoesNotExist:
            return Response({"usernameExists": False})


class CheckExistingEmailView(views.APIView):
    def get(self, request):
        email = request.query_params.get("email", None)

        if not email:
            return Response(
                {"error": "Email parameter is missing"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(email=email)
            return Response({"emailExists": True})
        except User.DoesNotExist:
            return Response({"emailExists": False})
