from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def validate_video(value):
    value= str(value)
    if value.startswith("https://www.youtube.com/watch?v=") != True : 
        raise ValidationError('sku')
    else:
        return value 