from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from common.models import CommonDateTimeModel, CommonNameModel


class RoomAmenity(models.Model):

    """Room Amenity Model Definition"""

    name = models.CharField(max_length=124, verbose_name=_("Name"))

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("Room Amenity")
        verbose_name_plural = _("Room Amenities")
        db_table = "amenities"


class RoomType(models.Model):

    """Room Type Model Definition"""

    class RoomTypeChoices(models.TextChoices):
        HOTEL = "hotel", _("Hotel")
        APARTMENT = "apartment", _("Apartment")
        CONDOMINIUM = "condominium", _("Condominium")
        VILLA = "villa", _("Villa")
        RESORT = "resort", _("Resort")
        CASTLE = "castle", _("Castle")
        BEACH_HOUSE = "beach", _("Beach House")
        LUXE = "luxe", _("Luxe")
        CABIN = "cabin", _("Cabin")
        CHATEAU = "cheateau", _("Chateau")
        MANSION = "mansion", _("Mansion")
        FARM = "farm", _("Farm")

    room_type = models.CharField(
        max_length=255,
        choices=RoomTypeChoices.choices,
        default=RoomTypeChoices.HOTEL,
        verbose_name=_("Room Type"),
    )

    def total_rooms(room_type):
        total_room_number = room_type.rooms.count()
        return total_room_number

    def __str__(self):
        return str(self.room_type)

    class Meta:
        verbose_name = _("Room Type")
        verbose_name_plural = _("Room Types")
        db_table = "room_types"


class RoomAddress(models.Model):

    """Room Address Model Definition"""

    country = models.ForeignKey(
        "cities_light.Country",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Country"),
        related_name="addresses",
    )
    city = models.ForeignKey(
        "cities_light.City",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("City"),
        related_name="addresses",
    )

    def __str__(self):
        return f"{self.city}, {self.country}"

    class Meta:
        verbose_name = _("Room Address")
        verbose_name_plural = _("Room Address")
        db_table = "room_addresses"


class Room(CommonDateTimeModel, models.Model):

    """Room Model Definition"""

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
    room_type = models.ForeignKey(
        "rooms.RoomType",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Room Type"),
        related_name="rooms",
    )
    guest = models.PositiveSmallIntegerField(
        verbose_name=_("Guest"),
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text=_(
            "Guest should include at least one person, and not exceed more than 100 people."
        ),
    )
    bedroom = models.PositiveSmallIntegerField(verbose_name=_("Bedroom"), default=1)
    bathroom = models.PositiveSmallIntegerField(verbose_name=_("Bathroom"), default=1)
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
        verbose_name=_("Owner"),
        related_name="rooms",
    )
    amenities = models.ManyToManyField(
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
        related_name="rooms",
    )
    address = models.OneToOneField(
        "rooms.RoomAddress",
        verbose_name=_("Address"),
        related_name="rooms",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    def total_reviews(room):
        total_number_reviews = room.reviews.count()
        return total_number_reviews

    total_reviews.short_description = _("Total reviews")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")
        db_table = "rooms"
