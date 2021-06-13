import json

from .models import Subscriptions
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def index(request):
    complete_subscriptions = Subscriptions.objects.all()
    complete_subscriptions = json.loads(serializers.serialize("json", complete_subscriptions))
    return render(request, "index.html", {"complete_subscriptions": complete_subscriptions})

@csrf_protect
def ajax_form(request):
    # complete_subscriptions = Subscriptions.objects.all()
    # complete_subscriptions = json.loads(serializers.serialize("json", complete_subscriptions))
    if request.method == "POST":
        ajax_data = json.loads(request.body)
        name = ajax_data.get("name", None)
        email = ajax_data.get("email", None)
        subscriptions = ajax_data.get("subscriptions", None)
        if name and email and subscriptions:
            subscriptions_model = Subscriptions(
                name=name,
                email=email,
                subscriptions=subscriptions
            )
            subscriptions_model.save()
            return HttpResponse(
                json.dumps({
                    "name": name,
                    "email": email,
                    "subscriptions": subscriptions
                }),
                content_type='application/json'
            )
