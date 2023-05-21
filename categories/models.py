from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CommonNameModel


class Category(CommonNameModel):

    """Category Model Definition"""

    pass

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        db_table = "categories"
