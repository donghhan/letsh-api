from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import *
from categories.models import Category
from users.models import *


class Room(TimeStampModel):

    """Rooms Model Definition"""

    name = models.CharField(max_length=200, verbose_name=_("Accomodation Name"))
    price_per_night = models.PositiveIntegerField(verbose_name=_("Price Per Night"))
    maximum_guests = models.PositiveSmallIntegerField(
        verbose_name=_("Maximum Number of Guests"), default=1
    )
    description = models.TextField(
        verbose_name=_("Room Description"), null=True, blank=True
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
        verbose_name=_("Owner"),
        related_name="rooms",
    )
    amenities = models.ManyToManyField("accomodations.Amenity", related_name="rooms")
    category = models.ForeignKey(
        "categories.Category", on_delete=models.DO_NOTHING, related_name="rooms"
    )

    def __str__(room):
        return room.name

    # Review score of customers
    """
    QuerySet is lazy, which is we are going to use only some of them.
    Intead of getting all QuerySet data, 
    """

    def rating(room):
        number_of_reviews = room.reviews.count()
        if number_of_reviews == 0:
            return 0
        else:
            total_rating = 0
            for review in room.reviews.all().values(
                "cleanliness", "communication", "accuracy"
            ):
                total_rating += (
                    review["cleanliness"] + review["communication"] + review["accuracy"]
                )
            return round(total_rating / 3)

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")
        db_table = "rooms"


class Amenity(models.Model):

    """Amenity Model Definition"""

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Amenity")
        verbose_name_plural = _("Amenities")
        db_table = "amenities"
