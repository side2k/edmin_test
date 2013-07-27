from django import forms

from edmin_test.models import Cinema, Presentation

class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema

class CinemaDeleteForm(forms.Form):
    confirmed = forms.BooleanField(initial=False, required=True)

class PresentationForm(forms.ModelForm):
    time = forms.DateTimeField(input_formats=['%H:%M'])
    def __init__(self, cinema_id, presentation_date, *args, **kwargs):
        return super(PresentationForm, self).__init_(*args, **kwargs)
    class Meta:
        model = Presentation