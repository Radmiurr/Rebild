from django import forms
from django.core.validators import RegexValidator

from .models import Reviews, User, Product



class ReviewForm(forms.ModelForm):

    alphanumeric = RegexValidator(r'[1-5]')

    rating = forms.CharField(max_length=1, validators=[alphanumeric])
    class Meta:
        model = Reviews
        fields = ("rating","text")
