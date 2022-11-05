import re
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from common.models import *


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(
        self,
        email,
        first_name,
        last_name,
        nickname,
        password,
    ):
        if not email:
            raise ValueError(_("You must provide a valid email address."))
        if not password:
            raise ValueError(_("You must provide a valid password."))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, nickname, password):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, TimeStampModel):

    """Custom User Definition Model"""

    class SexChioces(models.TextChoices):
        MALE = "male", _("Male")
        FEMALE = "female", _("Female")
        NOT_PREFER = "na", _("Prefer not to answer")

    class LanguageChoices(models.TextChoices):
        ENGLISH = "english", _("English")
        THAI = "thai", _("Thai")

    class CurrencyChoices(models.TextChoices):
        USD = "usd", _("US Dollar")
        THB = "thb", _("Thai Baht")

    email = models.EmailField(
        unique=True,
        max_length=100,
        help_text=_("Email address must be unique and valid."),
        error_messages={
            "null": _("You should provide an email address."),
            "blank": _("Email address cannot be empty."),
        },
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name=_("First Name"),
        blank=True,
        error_messages={
            "null": _("You should provide your first name."),
        },
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name=_("Last Name"),
        blank=True,
        error_messages={
            "null": _("You should provide your last name."),
        },
    )
    nickname = models.CharField(
        max_length=20,
        verbose_name=_("Nickname"),
        help_text=_(
            "Can only include lower/uppercases numbers, . and _. This nickname will be shown on the profile of the host. If not specified, first name field would appear."
        ),
    )
    phone_number = models.CharField(
        max_length=50,
        verbose_name=_("Phone Number"),
        null=True,
        blank=True,
    )
    profile_photo = models.ImageField(
        null=True, blank=True, verbose_name=_("Profile Photo")
    )
    sex = models.CharField(
        max_length=50,
        verbose_name=(_("Sex")),
        choices=SexChioces.choices,
        default=SexChioces.MALE,
    )
    language = models.CharField(
        max_length=10,
        verbose_name=(_("Language")),
        choices=LanguageChoices.choices,
        default=LanguageChoices.ENGLISH,
    )
    currency = models.CharField(
        max_length=10,
        verbose_name=(_("Currency")),
        choices=CurrencyChoices.choices,
        default=CurrencyChoices.USD,
    )
    is_host = models.BooleanField(default=False, verbose_name=_("Host"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active User"))
    is_admin = models.BooleanField(default=False, verbose_name=_("Admin User"))

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "nickname"]

    def __str__(self):
        return f"{self.first_name} ({self.email})"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        if self.is_admin:
            return True
        else:
            return False

    @property
    def is_staff(self):
        return self.is_admin

    def clean(self):
        # Check if either first name or last name includes characters other than alphabets.
        if type(self.first_name) != str:
            raise ValidationError(
                {
                    "first_name": _("First name can only include alphabets."),
                }
            )
        elif type(self.last_name) != str:
            raise ValidationError(
                {
                    "last_name": _("Last name can only include alphabets."),
                }
            )
        # Nickname validation
        unallowed_specials = "[\[$&+,:;=?@#|'<>-^*()%!\]\{\}\/]"
        invalid_special = re.findall(unallowed_specials, self.nickname)
        if len(invalid_special) != 0:
            raise ValidationError(
                {
                    "nickname": _(
                        "Nickname should contain only lower/uppercase of alphabets, numbers, . and _."
                    )
                }
            )
        elif len(self.nickname) < 2:
            raise ValidationError(
                {
                    "nickname": _(
                        "Nickname is too short. Should be no less than 2 characters."
                    )
                }
            )
        elif len(self.nickname) > 10:
            raise ValidationError(
                {
                    "nickname": _(
                        "Nickname is too long. Should be no less than 10 characters."
                    )
                }
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        db_table = "users"
