from rest_framework.serializers import ValidationError


def validate_link(value):
    if "youtube.com" not in value.lower():
        raise ValidationError("Ссылка на данный источник не допустима")
