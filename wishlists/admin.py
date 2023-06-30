from django.contrib import admin
from .models import *


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):

    """Wishlist Admin Model Definition"""

    list_display = ("name",)
