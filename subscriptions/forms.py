from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

class UnsubscribeForm(forms.Form):
    email = forms.EmailField()