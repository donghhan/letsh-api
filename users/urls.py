from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import *

urlpatterns = [
    path("", UserView.as_view()),
    path("my-profile", MyProfileView.as_view()),
    path("change-password", ChangePasswordView.as_view()),
    path("login", TokenObtainPairView.as_view()),
    path("logout", LogoutView.as_view()),
    path("<int:pk>", PublicUserView.as_view()),
    # JWT Auth
    path("token/refresh", TokenRefreshView.as_view()),
    path("token/verify", TokenVerifyView.as_view()),
]
