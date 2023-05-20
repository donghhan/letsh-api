from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from common.models import CommonDateTimeModel, CommonNameModel


class RoomAmenity(CommonNameModel):

    """Room Amenity Model Definition"""

    pass

    class Meta:
        verbose_name = _("Room Amenity")
        verbose_name_plural = _("Room Amenities")
        db_table = "amenities"


class Room(CommonDateTimeModel, models.Model):

    """Room Model Definition"""

    class RoomTypeChoices(models.TextChoices):
        APARTMENTS = "APARTMENTS", _("Apartments")
        VILLAS = "VILLAS", _("Villas")
        BEACH_HOUSE = "BEACH HOUSES", _("Beach Houses")
        HOTELS = "HOTELS", _("Hotels")
        RESORTS = "RESORTS", _("Resorts")

    name = models.CharField(
        max_length=50,
        verbose_name=_("Name"),
        help_text=_("Name of accomodation should not exceed more than 50 characters."),
    )
    price_per_night = models.PositiveSmallIntegerField(
        verbose_name=_("Price per night"),
        validators=[MinValueValidator(1)],
        help_text=_(
            "Value of price per night should always be more than 1 no matter of currency."
        ),
    )
    type = models.CharField(
        max_length=100,
        choices=RoomTypeChoices.choices,
        default=RoomTypeChoices.APARTMENTS,
    )
    guest = models.PositiveSmallIntegerField(
        verbose_name=_("Maximum guests allowed"),
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text=_(
            "Guest should include at least one person, and not exceed more than 100 people."
        ),
    )
    bedroom = models.PositiveSmallIntegerField(
        verbose_name=_("Number of bedrooms"), default=1
    )
    bathroom = models.PositiveSmallIntegerField(
        verbose_name=_("Number of bathrooms"), default=1
    )
    wifi = models.BooleanField(
        verbose_name=_("Wi-Fi"),
        help_text=_("Shows if Wi-Fi is available. Default is set to be True."),
        default=True,
    )
    description = models.TextField(
        verbose_name=_("Description"),
        null=True,
        blank=True,
        help_text=_("Can be omitted."),
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Owner"),
        related_name="rooms",
    )
    amenity = models.ManyToManyField(
        "rooms.RoomAmenity",
        null=True,
        blank=True,
        verbose_name=_("Amenities"),
        related_name="rooms",
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")
        db_table = "rooms"