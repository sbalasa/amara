from django import forms
from .models import Subscriptions

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriptions
        fields = ("name", "email", "subscription",)
        labels = {
                    "subscription": "Subscription type",
                    "name": "Customer Name",
                    "email": "Email"
                }

    def clean(self):
        cleaned_data = super().clean()