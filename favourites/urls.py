from django.urls import path
from .views import *

urlpatterns = [
    path("", AllFavouritesView.as_view()),
    path("<int:pk>", FavouriteDetailView.as_view()),
    path("<int:pk>/rooms/<int:room_pk>", FavouriteToggle.as_view()),
]
