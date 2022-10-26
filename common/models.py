from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampModel(models.Model):

    """TimeStamp Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RoomOptions(models.Model):

    """Room Option Model Definition"""

    name = models.CharField(max_length=200, verbose_name=_("Name"))
    icon = models.ImageField(null=True, blank=True)
    description = models.CharField(
        max_length=200,
        verbose_name=_("Description"),
        help_text=_("Short description of room option."),
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
