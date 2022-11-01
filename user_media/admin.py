from django.contrib import admin
from .models import *


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Model Definition"""

    list_display = ("file", "caption", "room")


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    """Video Admin Model Definition"""

    list_display = ("file", "room")
