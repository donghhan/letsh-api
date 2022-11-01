from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import *


class Favourites(TimeStampModel):

    """Favourite lists model definition"""

    name = models.CharField(max_length=200)
    rooms = models.ManyToManyField("accomodations.Room")
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Favourite")
        verbose_name_plural = _("Favourites")
        db_table = "favourites"
