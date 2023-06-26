from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from common.models import CommonDateTimeModel


class Review(CommonDateTimeModel):

    """Review model Definition"""

    cleanliness = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name=_("Cleanliness"),
        help_text=_("How clean a room was."),
    )
    accuracy = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name=_("Accuracy"),
        help_text=_("How much did host provide accurate information about room."),
    )
    location = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name=_("Location"),
        help_text=_("Was location good or fair enough to reach out?"),
    )
    communication = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name=_("Communication"),
        help_text=_("How well did room host communicate with customers?"),
    )
    check_in = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name=_("Check In"),
        help_text=_("How easy was it for checking in?"),
    )
    value = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name=_("Value"),
        help_text=_("Was it valuable enough compared to the price per night?"),
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.DO_NOTHING,
        related_name="reviews",
        verbose_name=_("Room"),
    )
    customer = models.ForeignKey(
        "users.User",
        on_delete=models.DO_NOTHING,
        related_name="reviews",
        verbose_name=_("Customer"),
    )
    comment = models.TextField(verbose_name=_("Comment"), null=True, blank=True)

    def get_average_rating(self):
        total_scores = (
            self.cleanliness
            + self.accuracy
            + self.location
            + self.communication
            + self.check_in
            + self.value
        )
        average_score = round(total_scores / 6, 2)
        return average_score

    def __str__(self):
        return str(f"{self.customer}'s review on {self.room}")

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        db_table = "reviews"
