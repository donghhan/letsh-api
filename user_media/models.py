from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import *


class Photo(TimeStampModel):

    """Photo Model Definition"""

    file = models.ImageField(null=True, blank=True)
    caption = models.CharField(max_length=250, null=True, blank=True)
    room = models.ForeignKey(
        "accomodations.Room", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.file

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")
        db_table = "photo"


class Video(TimeStampModel):

    """Video Model Definition"""

    file = models.FileField(null=True, blank=True)
    caption = models.CharField(max_length=250, null=True, blank=True)
    room = models.OneToOneField(
        "accomodations.Room", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.file

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")
        db_table = "video"
