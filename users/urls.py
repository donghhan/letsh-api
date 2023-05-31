from django.urls import path
from . import views


urlpatterns = [
    path("my-profile/", views.MyProfileView.as_view()),
    path("change-password/", views.ChangePasswordView.as_view()),
    path("login/", views.LoginView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path("", views.UserView.as_view()),
]
