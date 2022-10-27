from django.contrib import admin
from .models import *


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    """Review Admin Model"""

    list_display = ("date", "review", "room")
