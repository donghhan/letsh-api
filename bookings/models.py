from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class Booking(models.Model):

    """Booking Model Definition"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="booking",
    )
    room = models.ForeignKey(
        "accomodations.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="booking",
    )
    check_in = models.DateField(verbose_name=_("Checking in"))
    check_out = models.DateField(verbose_name=_("Checking out"))
    guests = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.user.nickname

    class Meta:
        verbose_name = _("Booking")
        verbose_name_plural = _("Bookings")
        db_table = "booking"
