from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import TimeStampModel


class Category(TimeStampModel):

    """Category Model Definition"""

    class CategoryKindChoices(models.TextChoices):
        ROOM = ("room", "Room")
        HOUSE = ("house", "House")
        HOTEL_APARTMENT = ("hotel", "Hotel Apartments")
        PARKING = ("parking", "Parking")
        MOBILE = ("mobile", "Mobile")

    name = models.CharField(max_length=20)
    kind = models.CharField(
        max_length=20,
        choices=CategoryKindChoices.choices,
        default=CategoryKindChoices.ROOM,
    )

    def __str__(self):
        return f"{self.kind}: {self.name}"

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        db_table = "categories"
