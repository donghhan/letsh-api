from django.urls import path
from .views import *

urlpatterns = [
    path("", UserView.as_view()),
    path("my-profile", MyProfileView.as_view()),
    path("change-password", ChangePasswordView.as_view()),
    path("login", LoginView.as_view()),
    path("logout", LogoutView.as_view()),
    path("<int:pk>", PublicUserView.as_view()),
]
