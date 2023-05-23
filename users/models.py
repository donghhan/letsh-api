from django.db import models
from django.contrib.admin import display
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    """User Model Definition"""

    class SexChoices(models.TextChoices):
        MALE = "Male", _("Male")
        FEMALE = "Female", _("Female")
        UNKNOWN = "Unknown", _("Unknown")

    mobile_number = models.CharField(
        max_length=128, verbose_name=_("Mobile Number"), null=True, blank=True
    )
    sex = models.CharField(
        max_length=20,
        verbose_name=_("Sex"),
        choices=SexChoices.choices,
        default=SexChoices.MALE,
    )

    def __str__(self):
        return str(self.username)

    @property
    @display(description="Full Name")
    def get_full_name(self):
        return super().get_full_name()
