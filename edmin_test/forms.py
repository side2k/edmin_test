from datetime import datetime

from django import forms

from edmin_test.models import Cinema, Presentation

class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema

class ConfirmationForm(forms.Form):
    confirmed = forms.BooleanField(initial=False, required=True)

class PresentationForm(forms.ModelForm):
    time = forms.DateTimeField(input_formats=['%H:%M'])

    def __init__(self, cinema_id, presentation_date, *args, **kwargs):
        instance = super(PresentationForm, self).__init__(*args, **kwargs)
        self.cinema_id = cinema_id
        self.presentation_date = presentation_date
        self.fields['cinema'].required = False
        return instance

    def clean_time(self):
        time = self.cleaned_data['time']
        time = datetime.combine(self.presentation_date.date(), time.time())
        return time

    def save(self, *args, **kwargs):
        return super(PresentationForm, self).save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        cleaned_data = super(PresentationForm, self).clean(*args, **kwargs)
        self.cleaned_data['cinema'] = Cinema.objects.get(id=self.cinema_id)
        return cleaned_data

    class Meta:
        model = Presentation