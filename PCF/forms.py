from django import forms
from django.forms import ModelForm, Textarea
from .models import Subscriptions

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriptions
        fields = '__all__'
        labels = {
                    "subscription": "Subscription type",
                    "name": "Customer Name",
                    "email": "Email"
                }

    def clean(self):
        cleaned_data = super().clean()