from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from common.models import *
from categories.models import *


class Parking(TimeStampModel):

    """Parking Model Definition"""

    name = models.CharField(max_length=200)
    maximum_capacity = models.PositiveSmallIntegerField(
        verbose_name=_("Maximum Capacity"), validators=[MinValueValidator(1)]
    )
    category = models.ForeignKey(
        "categories.Category", on_delete=models.DO_NOTHING, related_name="parkings"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Parking")
        verbose_name_plural = _("Parkings")
        db_table = "parking"
