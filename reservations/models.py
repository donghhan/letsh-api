from django.utils.timezone import now
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CommonDateTimeModel


class Reservation(CommonDateTimeModel, models.Model):

    """Reservation Model Definition"""

    guest = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Reserved guest"),
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Room"),
    )
    adult = models.PositiveSmallIntegerField(
        verbose_name=_("Number of adults"), default=2
    )
    children = models.PositiveSmallIntegerField(
        verbose_name=_("Number of children"), null=True, blank=True, default=0
    )
    check_in = models.DateField(verbose_name=_("Check-in date"), default=now)
    check_out = models.DateField(verbose_name=_("Check-out date"))

    def __str__(self):
        return str(self.guest.username)

    class Meta:
        verbose_name = _("Reservation")
        verbose_name_plural = _("Reservations")
        db_table = "reservations"
