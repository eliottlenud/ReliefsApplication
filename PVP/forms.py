from django import forms
from PVP.validators import validate_video
from django.core.validators import URLValidator


class YTForm(forms.Form):
	link = forms.URLField(label='')