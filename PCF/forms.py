from django import forms

class AjaxForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length = 254)
    subscriptions = forms.CharField(max_length=20)
