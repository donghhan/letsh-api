from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    """Category Model Definition"""

    name = models.CharField(max_length=128, verbose_name=_("Category name"))

    # Get total number of rooms below the chosen category
    def get_total_room_by_categories(category):
        total_room_number = category.rooms.count()
        return total_room_number

    get_total_room_by_categories.short_description = _("Total rooms")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        db_table = "categories"
