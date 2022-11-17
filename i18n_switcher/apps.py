from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class I18NSwitcherConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "i18n_switcher"
    verbose_name = _("I18N Switcher")
