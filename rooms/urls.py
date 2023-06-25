from django.urls import path
from . import views

urlpatterns = [
    path("amenities/", views.RoomAmenityView.as_view()),
    path("amenities/<int:pk>", views.RoomAmenityDetailView.as_view()),
    path("room-types/", views.RoomTypeView.as_view()),
    path(
        "room-types/<int:pk>",
        views.RoomTypeDetailView.as_view(),
        name="room_type_detail",
    ),
    path("", views.RoomView.as_view()),
    path("<int:pk>", views.RoomDetailView.as_view()),
    path("<int:pk>/reservations/", views.RoomReservationView.as_view()),
    path("<int:pk>/photos/", views.RoomPhotoView.as_view(), name="room-photos"),
]
