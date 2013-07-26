from django import forms

from edmin_test.models import Cinema

class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema

class CinemaDeleteForm(forms.Form):
    confirmed = forms.BooleanField(initial=False, required=True)