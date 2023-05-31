from django.urls import path
from . import views


urlpatterns = [
    path("my-profile/", views.MyProfileView.as_view()),
    path("", views.UserView.as_view()),
]
