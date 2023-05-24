from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    """Category Model Definition"""

    name = models.CharField(max_length=128, verbose_name=_("Category name"))

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        db_table = "categories"
