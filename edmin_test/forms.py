from django import forms

from edmin_test.models import Cinema

class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema