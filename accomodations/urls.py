from django.urls import path
from .views import *

urlpatterns = [
    path("", AllRoomsView.as_view()),
    path("<int:pk>/", RoomDetailView.as_view()),
    path("<int:pk>/reviews", RoomReviewView.as_view()),
    path("amenities/", AllAmenitiesView.as_view()),
    path("amenities/<int:pk>", AmenityDetailView.as_view()),
]
