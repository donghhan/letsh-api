from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import *
from users.models import *


class Room(TimeStampModel):

    """Rooms Model Definition"""

    class RoomCategoryChoices(models.TextChoices):
        HOTEL = "hotel", _("Hotel")
        HOUSE = "house", _("House")
        APARTMENT = "apartment", _("Apartment")
        GUESTHOUSE = "guesthouse", _("Guesthouse")

    name = models.CharField(max_length=200, verbose_name=_("Accomodation Name"))
    room_category = models.CharField(
        max_length=20,
        verbose_name=_("Room Category"),
        choices=RoomCategoryChoices.choices,
        default=RoomCategoryChoices.HOTEL,
    )
    price_per_night = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Price Per Night")
    )
    maximum_guests = models.PositiveSmallIntegerField(
        verbose_name=_("Maximum Number of Guests"), default=1
    )
    number_of_beds = models.PositiveSmallIntegerField(
        verbose_name=_("Number of beds"), default=1
    )
    number_of_bedrooms = models.PositiveSmallIntegerField(
        verbose_name=_("Number of Bedrooms"), default=1
    )
    number_of_bathrooms = models.PositiveSmallIntegerField(
        verbose_name=_("Numeber of Bathrooms"), default=1
    )
    is_free_breakfast = models.BooleanField(
        verbose_name=_("Free Breakfast"), default=False
    )
    is_free_internet = models.BooleanField(
        verbose_name=_("Free Internet"), default=False
    )
    is_free_parking = models.BooleanField(verbose_name=_("Free Parking"), default=False)
    is_free_booking_cancelation = models.BooleanField(
        verbose_name=_("Free Booking Cancelation"), default=True
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Owner"),
        related_name="rooms",
    )
    amenities = models.ManyToManyField("accomodations.Amenity", related_name="rooms")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")
        db_table = "rooms"


class Amenity(TimeStampModel, RoomOptions):

    """Amenity Model Definition"""

    pass

    class Meta:
        verbose_name = _("Amenity")
        verbose_name_plural = _("Amenities")
        db_table = "amenities"
