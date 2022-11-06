from django.urls import path
from .views import *

urlpatterns = [path("<int:pk>", PhotoDetailView.as_view())]
