from django.urls import path
from rest_framework_simplejwt import views
from . import views

urlpatterns = [
    path("", views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", views.TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "decorated/token-obtain",
        views.DecoratedTokenObtainPairView.as_view(),
        name="decoreated_token_obtain",
    ),
]
