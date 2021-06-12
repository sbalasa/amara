import json

from .forms import AjaxForm
from .models import Subscriptions
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def ajax_form(request):
    complete_subscriptions = Subscriptions.objects.all()

    if request.method == "POST" and request.is_ajax():
        ajax_data = json.loads(request.body)
        name = ajax_data.get("name", None)
        email = ajax_data.get("email", None)
        subscriptions = ajax_data.get("subscriptions", None)
        if name and email and subscriptions:
            form = AjaxForm(request.POST)
            if form.is_valid():
                subscriptions_model = Subscriptions(
                    name=name,
                    email=email,
                    subscriptions=subscriptions
                )
                subscriptions_model.save()
                return render(request, "index.html", {"complete_subscriptions": complete_subscriptions})
    return render(request, "index.html", {"complete_subscriptions": complete_subscriptions})
