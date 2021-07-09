
from django.core.exceptions import ValidationError


def validate_judul(value):
    if value in ['llano','ujang','dadang']:
        raise ValidationError(f"{ value } tidak boleh")

