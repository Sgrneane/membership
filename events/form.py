from django import forms
from .models import Event, TicketType
from django.forms import modelformset_factory


# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         exclude = [
#             'veneu',
#             'url_location',
#             'description',
#             'guest_description',
#             #'ticket_pricing_description'
#             'status',
#             'groups',
#             'pricing_type',
#             'pricing_description', 
#             'pricing_normal', 
#             'pricing_vip', 
#             'pricing_vvip'


#         ]

# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['name', 'date', 'duration', 'type', 'veneu', 'url_location', 'description', 'guest_description', 'pricing_type', 'banner', 'groups']
    

# TicketTypeFormSet = modelformset_factory(TicketType, fields=('name', 'description', 'limit', 'price'), extra=1)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'duration', 'type', 'veneu', 'url_location', 'description', 'guest_description', 'pricing_type','status' ,'ticket_pricing_description','banner', 'groups']


class TicketTypeForm(forms.ModelForm):
    class Meta:
        model = TicketType
        fields ='__all__'
TicketTypeFormSet = modelformset_factory(TicketType, fields=('name', 'description', 'limit', 'price'), extra=1)