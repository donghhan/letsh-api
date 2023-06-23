from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()

router.register(r"room-type", views.RoomTypeViewset, basename="room-type-thumbnail")
urlpatterns = router.urls
