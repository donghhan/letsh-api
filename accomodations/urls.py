from django.urls import path
from .views import *

urlpatterns = [
    path("", RoomsView.as_view()),
    path("<int:pk>/", RoomDetailView.as_view()),
    path("<int:pk>/reviews", RoomReviewView.as_view()),
    path("<int:pk>/photos", RoomPhotoView.as_view()),
    path("<int:pk>/bookings", RoomBookingView.as_view()),
    path("amenities/", AmenitiesView.as_view()),
    path("amenities/<int:pk>", AmenityDetailView.as_view()),
]
