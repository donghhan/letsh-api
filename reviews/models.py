from django.db import models
from django.db.models import Sum, Count
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from common.models import CommonDateTimeModel


class Review(CommonDateTimeModel):

    """Review model Definition"""

    cleanliness = cleanliness = models.PositiveSmallIntegerField(
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
        null=True,
        blank=True,
    )
    comment = models.TextField(verbose_name=_("Comment"), null=True, blank=True)

    def average_cleanliness(self):
        total_cleanliness_score = Review.objects.aggregate(Sum("cleanliness"))[
            "cleanliness__sum"
        ]
        number_of_room = Review.objects.annotate(num_rooms=Count("room")).count()
        average_cleanliness = (
            f"{round(total_cleanliness_score / number_of_room, 2):.2f}"
        )
        return average_cleanliness

    def average_accuracy(self):
        total_accuracy_score = Review.objects.aggregate(Sum("accuracy"))[
            "accuracy__sum"
        ]
        number_of_room = Review.objects.annotate(num_rooms=Count("room")).count()
        average_accuracy = f"{round(total_accuracy_score / number_of_room, 2):.2f}"
        return average_accuracy

    def average_location(self):
        total_location_score = Review.objects.aggregate(Sum("location"))[
            "location__sum"
        ]
        number_of_room = Review.objects.annotate(num_rooms=Count("room")).count()
        average_location = f"{round(total_location_score / number_of_room, 2):.2f}"
        return average_location

    def average_communication(self):
        total_location_score = Review.objects.aggregate(Sum("communication"))[
            "communication__sum"
        ]
        number_of_room = Review.objects.annotate(num_rooms=Count("room")).count()
        average_communication = f"{round(total_location_score / number_of_room, 2):.2f}"
        return average_communication

    def average_check_in(self):
        total_check_in_score = Review.objects.aggregate(Sum("check_in"))[
            "check_in__sum"
        ]
        number_of_room = Review.objects.annotate(num_rooms=Count("room")).count()
        average_check_in = f"{round(total_check_in_score / number_of_room, 2):.2f}"
        return average_check_in

    def average_value(self):
        total_value_score = Review.objects.aggregate(Sum("value"))["value__sum"]
        number_of_room = Review.objects.annotate(num_rooms=Count("room")).count()
        average_value = f"{round(total_value_score / number_of_room, 2):.2f}"
        return average_value

    def average_total_rating(self):
        rating_fields = [
            self.average_cleanliness(),
            self.average_accuracy(),
            self.average_location(),
            self.average_communication(),
            self.average_check_in(),
            self.average_value(),
        ]

        rating_values = [eval(rating) for rating in rating_fields if rating is not None]

        if rating_values:
            total_scores = sum(rating_values)
            average_score = round(total_scores / len(rating_values), 2)
            return average_score

        return None

    average_total_rating.short_description = _("Average Rating")

    def __str__(self):
        return str(f"{self.customer}'s review on {self.room}")

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        db_table = "reviews"
