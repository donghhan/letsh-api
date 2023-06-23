from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from common.models import CommonDateTimeModel


class RoomTypeThumbnail(CommonDateTimeModel):

    """Photo Model Definition"""

    file = models.ImageField(verbose_name=_("Photo file"))
    room_type = models.ForeignKey(
        "rooms.RoomType",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Photos for room_type"),
    )

    def __str__(self):
        return str(self.file)

    class Meta:
        verbose_name = "Photo for room type"
        verbose_name_plural = "Photos for room type"
        db_table = "photo_room_type"
