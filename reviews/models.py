from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from users.models import *
from accomodations.models import *


class Review(models.Model):

    """Review Model Definition"""

    date = models.DateField(auto_now_add=True, null=True, blank=True)
    review = models.TextField()
    # Individual review scores
    cleanliness = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=5
    )
    communication = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=5
    )
    accuracy = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=5
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="reviews",
    )
    room = models.ForeignKey(
        "accomodations.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )

    def __str__(self):
        return str(self.user.nickname)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        db_table = "reviews"
