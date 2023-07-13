from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CommonDateTimeModel


class RoomPhoto(CommonDateTimeModel):

    """Room Photo Model Definition"""

    photo = models.URLField(verbose_name=_("Photo"), null=True, blank=True)
    thumbnail = models.URLField(verbose_name=_("Thumbnail Image"))
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Room"),
        related_name="rooms",
    )

    def __str__(self):
        return str(f"{self.room.name}'s photos")

    class Meta:
        verbose_name = "Photo for room"
        verbose_name_plural = "Photos for room"
        db_table = "photo_room"
