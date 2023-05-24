from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from common.models import CommonDateTimeModel, CommonNameModel


class RoomAmenity(models.Model):

    """Room Amenity Model Definition"""

    name = models.CharField(max_length=124, verbose_name=_("Name"))
    icon = models.ImageField(null=True, blank=True, verbose_name=_("Icon"))

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("Room Amenity")
        verbose_name_plural = _("Room Amenities")
        db_table = "amenities"


class Room(CommonDateTimeModel, models.Model):

    """Room Model Definition"""

    class RoomTypeChoices(models.TextChoices):
        APARTMENTS = "Apartments", _("Apartments")
        VILLAS = "Villas", _("Villas")
        BEACH_HOUSE = "Beach Houses", _("Beach Houses")
        HOTELS = "Hotels", _("Hotels")
        RESORTS = "Resorts", _("Resorts")

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
    room_type = models.CharField(
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
        verbose_name=_("Amenities"),
        related_name="rooms",
        blank=True,
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.DO_NOTHING,
        verbose_name=_("Category"),
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")
        db_table = "rooms"
