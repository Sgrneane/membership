from django import forms
from .models import Groups,Notifications

class CreateGroupForm(forms.ModelForm):

    class Meta:
        model = Groups
        fields = ['name','description','users']
    

class NotificationForm(forms.ModelForm):

    class Meta:
        model = Notifications
        fields =['subject','description','groups','status']
