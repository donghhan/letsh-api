from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from .models import *


class WishlistView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass

    def post(self, request):
        pass
