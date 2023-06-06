from django.urls import path
from .views import *


urlpatterns = [
    path("amenities/", RoomAmenityView.as_view()),
    path("amenities/<int:pk>", RoomAmenityDetailView.as_view()),
    path("", RoomView.as_view()),
    path("<int:pk>", RoomDetailView.as_view()),
    path("<int:pk>/reservations/", RoomReservationView.as_view()),
]
