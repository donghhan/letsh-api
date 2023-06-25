from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()

router.register(r"", views.CategoryViewset, basename="room_categories")

urlpatterns = [path("<int:pk>/rooms", views.SimplifiedRoomByCategories.as_view())]


urlpatterns = router.urls + urlpatterns
