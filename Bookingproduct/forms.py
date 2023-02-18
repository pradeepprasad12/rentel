from django import forms
from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['product', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
