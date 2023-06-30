from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CommonDateModel


class Wishlist(CommonDateModel):

    """Wishlist Model Definition"""

    name = models.CharField(max_length=128, verbose_name=_("Wishlist name"))
    user = models.ForeignKey(
        "users.User",
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="wishlists",
    )
    room = models.ManyToManyField("rooms.Room", related_name="wishlists")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("Wishlist")
        verbose_name_plural = _("Wishlists")
        db_table = "wishlists"
