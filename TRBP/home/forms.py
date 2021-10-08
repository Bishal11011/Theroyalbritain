from django.forms import ModelForm, widgets
from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {'arival': DateInput()}

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'










