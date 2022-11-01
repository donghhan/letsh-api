from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *


@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):

    """Favourites admin model definition"""

    list_display = ("name", "user", "created_at", "updated_at")
    list_per_page = 50
