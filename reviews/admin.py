from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    """Review Admin Model"""

    list_display = (
        "reviewer_nickname",
        "date",
        "review",
        "room",
        "cleanliness",
        "communication",
        "accuracy",
        "get_individual_review_score",
    )
    list_filter = ("user__is_host", "cleanliness", "communication", "accuracy")
    search_fields = ("room__name", "nickname")
    search_help_text = "Searching avilable with room name and user's nickname."

    def reviewer_nickname(self, obj):
        return obj.user.nickname

    reviewer_nickname.short_description = "nickname"

    def get_individual_review_score(self, obj):
        total_individual_score = obj.cleanliness + obj.communication + obj.accuracy
        return round(total_individual_score / 3, 2)

    get_individual_review_score.short_description = "total average score"
