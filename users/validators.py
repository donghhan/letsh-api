from django.core.exceptions import ValidationError


class CustomPasswordValidator:
    def validate(self, password, user=None):
        MIN_LENGTH = 1
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"

        if not any(c.isdigit() for c in password):  # 1
            raise ValidationError(f"Password must contain at least {MIN_LENGTH} digit.")
        if not any(c.isalpha() for c in password):  # 2
            raise ValidationError(
                f"Password must contain at least {MIN_LENGTH} character."
            )
        if not any(c.isupper() for c in password):  # 3
            raise ValidationError(
                f"Password must contain at least {MIN_LENGTH} uppercase."
            )
        if not any(c in special_characters for c in password):  # 4
            raise ValidationError(
                f"Password must contain at least {MIN_LENGTH} special characters."
            )

    def get_help_text(self):
        return "Password should be no less than 8 characters with including at least 1 uppercase, lowercase, number and special character."
