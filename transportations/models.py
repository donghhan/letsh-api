from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import *


class Features(CommonNameModel):

    """Transportation Features Model Definition"""

    pass

    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")
        db_table = "transportation_features"


class Policies(models.Model):

    """Transportation Policies Model Definition"""

    pass

    class Meta:
        verbose_name = _("Policy")
        verbose_name_plural = _("Policies")
        db_table = "transportation_policies"


class Transportation(TimeStampModel):

    """Transportation Model Definition"""

    class GearTypeChoices(models.TextChoices):
        MANUAL = "manual", _("Manual")
        AUTO = "auto", _("Auto")
        ELECTRIC = "electirc", _("Electric")

    class TransportationTypeChoices(models.TextChoices):
        SMALL = "small", _("Small")
        MEDIUM = "medium", _("Medium")
        LARGE = "large", _("Large")
        LUXURY = "luxury", _("Luxury")
        PEOPLE_CARRIER = "people_carrier", _("People Carrier")
        SUV = "suv", _("SUV")
        VAN = "van", _("Van")

    name = models.CharField(max_length=200, verbose_name=_("Name of Transportation"))
    price_per_night = models.PositiveSmallIntegerField(
        verbose_name=_("Price per Night"), help_text=_("Amount should be in THB.")
    )
    is_free_cancelation = models.BooleanField(
        default=False, verbose_name=_("Free Cancelation")
    )
    seats = models.PositiveSmallIntegerField(
        verbose_name=_("Maximum number of people affordable")
    )
    bag = models.PositiveSmallIntegerField(
        verbose_name=_("Maximum number of bags affordable"), null=True, blank=True
    )
    is_air_conditioned = models.BooleanField(
        verbose_name=_("Is air-conditioner installed"), default=True
    )
    number_of_doors = models.PositiveSmallIntegerField(
        verbose_name=_("Number of doors"), null=True, blank=True
    )
    gear_type = models.CharField(
        max_length=10,
        verbose_name=_("Gear Type"),
        choices=GearTypeChoices.choices,
        default=GearTypeChoices.AUTO,
    )
    car_type = models.CharField(
        max_length=20,
        verbose_name=_("Car Type"),
        choices=TransportationTypeChoices.choices,
        default=TransportationTypeChoices.SMALL,
    )
    features = models.ForeignKey(
        Features,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Features"),
        related_name="transportation",
    )
    policies = models.ForeignKey(
        Policies,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Policies"),
        related_name="transportation",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Transportation")
        verbose_name_plural = _("Transportations")
        db_table = "transportations"
