from django import forms
from .models import MyModel


class NameForm(forms.Form):
    """
    Form for collecting first and last names.
    """
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)