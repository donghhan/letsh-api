from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class Booking(models.Model):

    """Booking Model Definition"""

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, null=True, blank=True
    )
    rooms = models.ForeignKey(
        "accomodations.Room", on_delete=models.CASCADE, null=True, blank=True
    )
    check_in = models.DateTimeField(verbose_name=_("Checking in"))
    check_out = models.DateTimeField(verbose_name=_("Checking out"))
    guests = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.user.nickname

    class Meta:
        verbose_name = _("Booking")
        verbose_name_plural = _("Bookings")
        db_table = "booking"
