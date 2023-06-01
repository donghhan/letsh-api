import uuid
from datetime import datetime
from django.core.validators import MinValueValidator
from django.utils.timezone import now
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CommonDateTimeModel


class Reservation(CommonDateTimeModel, models.Model):

    """Reservation Model Definition"""

    def reservation_id_generator():
        reservation_created_time = str(datetime.now().date()).replace("-", "")
        reservation_code = uuid.uuid4().hex[:6].upper()
        reservation_id = reservation_created_time + reservation_code
        return reservation_id

    reservation_id = models.SlugField(
        unique=True,
        primary_key=True,
        editable=False,
        max_length=20,
        default=reservation_id_generator(),
    )
    guest = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name=_("Reserved guest"),
        related_name="reservations",
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Room"),
        related_name="reservations",
    )
    adult = models.PositiveSmallIntegerField(
        verbose_name=_("Number of adults"), validators=[MinValueValidator(1)], default=2
    )
    children = models.PositiveSmallIntegerField(
        verbose_name=_("Number of children"), null=True, blank=True, default=0
    )
    check_in = models.DateField(verbose_name=_("Check-in date"), default=now)
    check_out = models.DateField(verbose_name=_("Check-out date"))

    def __str__(self):
        return str(self.reservation_id)

    class Meta:
        verbose_name = _("Reservation")
        verbose_name_plural = _("Reservations")
        db_table = "reservations"
