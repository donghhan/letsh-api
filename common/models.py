from django.db import models
from django.utils.translation import gettext_lazy as _


class CommonDateModel(models.Model):

    """
    Common Date Model Definition: Only contains date model
    - created_date: Created date time
    - updated_date: Updated date time
    """

    created_date = models.DateField(auto_now_add=True, verbose_name=_("Created Date"))
    updated_date = models.DateField(auto_now=True, verbose_name=_("Updated Date"))

    class Meta:
        abstract = True


class CommonDateTimeModel(models.Model):

    """
    Common Date Time Model Definition: Contains both date and time
    - created_at: Created date and time
    - updated_at: Updated date and time
    """

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created Date & Time")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated Date & Time")
    )

    class Meta:
        abstract = True


class CommonNameModel(models.Model):

    """
    Common Name Model Definition
    - Used for creating the individual items (i.e. amenities, etc.)
    """

    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        abstract = True
