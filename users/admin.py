from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import *


@admin.action(description="Convert activity of selected users.")
def set_activity(modeladmin, request, users):
    for user in users.all():
        if user.is_active == False:
            user.is_active = True
            user.save()
        else:
            user.is_active = False
            user.save()


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError(_("Passwords do not match."))

        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    """User Admin Definition"""

    add_form = UserCreationForm

    list_display = (
        "nickname",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "sex",
        "language",
        "currency",
        "is_host",
        "is_active",
    )
    list_filter = (
        "sex",
        "language",
        "currency",
        "is_host",
        "is_active",
    )
    list_per_page = 50
    radio_fields = {"sex": admin.HORIZONTAL}
    search_fields = ["nickname", "email", "phone_number"]
    search_help_text = "Searching avilable with nickname, email and phone number."
    fieldsets = (
        (
            "Personal Information",
            {
                "classes": "wide",
                "fields": (
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "nickname",
                    "sex",
                    "phone_number",
                ),
            },
        ),
        (
            "Preference",
            {
                "classes": "wide",
                "fields": (
                    "language",
                    "currency",
                ),
            },
        ),
        (
            "Status",
            {
                "classes": ("collapse",),
                "fields": (
                    "is_host",
                    "is_active",
                    "is_admin",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            "Personal Information",
            {
                "classes": "wide",
                "fields": (
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "nickname",
                    "sex",
                    "phone_number",
                ),
            },
        ),
        (
            "Preference",
            {
                "classes": "wide",
                "fields": (
                    "language",
                    "currency",
                ),
            },
        ),
        (
            "Status",
            {
                "classes": ("collapse",),
                "fields": (
                    "is_host",
                    "is_active",
                    "is_admin",
                ),
            },
        ),
    )
    empty_value_display = "(unknown)"
    ordering = ("email",)
    filter_horizontal = ()
    actions = [set_activity]

    admin.site.index_title = _("User Admin Page")
    admin.site.site_title = _("User Site Management")
