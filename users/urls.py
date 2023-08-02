from django.urls import path
from . import views


urlpatterns = [
    path("my-profile/", views.MyProfileView.as_view()),
    path("change-password/", views.ChangePasswordView.as_view()),
    path(
        "check-username/",
        views.CheckExistingUsernameView.as_view(),
        name="check-username",
    ),
    path(
        "check-email",
        views.CheckExistingEmailView.as_view(),
        name="check-email",
    ),
    path("login/", views.LoginView.as_view()),
    path("logout", views.LogoutView.as_view()),
    path("line", views.LineLoginView.as_view()),
    path("signup/", views.SignupView.as_view()),
]
