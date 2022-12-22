from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampModel(models.Model):

    """TimeStamp Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CommonNameModel(models.Model):

    """Common Name Model Definition"""

    """
    This model is just for naming variety of choices such as
    amenities, features, etc...
    """

    name = models.CharField(max_length=100, verbose_name=_("Name of item"))

    def __str__(self):
        return self.name
