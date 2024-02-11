from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = [
            'veneu',
            'url_location',
            'description',
            'guest_description',
            'ticket_pricing_description'
            'status',
        ]