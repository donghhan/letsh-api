from django.contrib import admin
from django.db.models import Q, F
from django.utils.translation import gettext_lazy as _
from .models import *


class RoomScoreFilter(admin.SimpleListFilter):
    title = _("Room Score")
    parameter_name = "score"

    def lookups(self, request, model_admin):
        return [
            ("1", _("Very poor")),
            ("2", _("Poor")),
            ("3", _("Normal")),
            ("4", _("Good")),
            ("5", _("Excellent")),
        ]

    def queryset(self, request, queryset):
        queryset = queryset.alias(
            total_score=(
                F("cleanliness")
                + F("accuracy")
                + F("location")
                + F("communication")
                + F("check_in")
                + F("value")
            )
        )
        if self.value() == "1":
            return queryset.filter(total_score__gte=6, total_score__lt=12)
        if self.value() == "2":
            return queryset.filter(total_score__gte=12, total_score__lt=18)
        if self.value() == "3":
            return queryset.filter(total_score__gte=18, total_score__lt=24)
        if self.value() == "4":
            return queryset.filter(total_score__gte=24, total_score__lt=30)
        if self.value() == "5":
            return queryset.filter(total_score__exact=30)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    empty_value_display = "-----"
    fieldsets = [
        (
            "Room",
            {
                "fields": [
                    "room",
                ]
            },
        ),
        (
            "Evaluation",
            {
                "fields": ["average_total_rating", "comment", "customer"],
                "classes": "wide",
            },
        ),
        (
            "Individual Scores",
            {
                "fields": [
                    "cleanliness",
                    "accuracy",
                    "location",
                    "communication",
                    "check_in",
                    "value",
                ]
            },
        ),
        (
            "Average Scores",
            {
                "fields": [
                    "average_cleanliness",
                    "average_accuracy",
                    "average_location",
                    "average_communication",
                    "average_check_in",
                    "average_value",
                ],
            },
        ),
    ]
    list_display = (
        "room",
        "customer",
        "cleanliness",
        "accuracy",
        "location",
        "communication",
        "check_in",
        "value",
        "average_total_rating",
        "comment",
    )
    list_display_links = ("room",)
    list_per_page = 20
    list_filter = [RoomScoreFilter]
    search_fields = ("room__name", "customer__username")
    search_help_text = _("Searchable by room name and user ID.")
    readonly_fields = (
        "average_total_rating",
        "average_cleanliness",
        "average_accuracy",
        "average_location",
        "average_communication",
        "average_check_in",
        "average_value",
    )

    @admin.display(description="Customer review")
    def get_customer_username(self, obj):
        return obj.customer.name

    @admin.display(description=_("Average Cleanliness Score"))
    def get_average_cleanliness(self, obj):
        pass

    def get_average_score(self, obj):
        print(obj.get_average_rating)
        return obj.get_average_rating
