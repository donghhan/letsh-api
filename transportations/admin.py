from django.contrib import admin
from .models import *


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):

    """Features Model Admin"""

    list_display = ("feature_name", "icon")
    list_per_page = 10
    empty_value_display = "(unknown)"
    search_fields = ("feature_name",)


@admin.register(Policies)
class PolicyAdmin(admin.ModelAdmin):

    """Policy Model Admin"""

    list_display = ("policy",)
    list_per_page = 10
    empty_value_display = "(unknown)"
    search_fields = ("policy",)


@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):

    """Transportation Model Admin"""

    list_display = (
        "name",
        "price_per_night",
        "seats",
        "bag",
        "number_of_doors",
        "gear_type",
        "car_type",
        "features",
        "policies",
        "is_air_conditioned",
    )
