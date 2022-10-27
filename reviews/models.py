from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import *
from accomodations.models import *


class Review(models.Model):

    """Review Model Definition"""

    date = models.DateField(auto_now_add=True, null=True, blank=True)
    review = models.TextField()
    cleanliness = models.PositiveSmallIntegerField(null=True, blank=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.DO_NOTHING, null=True, blank=True
    )
    room = models.ForeignKey(
        "accomodations.Room", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.reviewer.name

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        db_table = "reviews"
