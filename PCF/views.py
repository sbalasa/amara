import json

from .models import Subscriptions
from .forms import SubscriptionForm

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def index(request):
    complete_subscriptions = Subscriptions.objects.all()
    # complete_subscriptions = json.loads(serializers.serialize("json", complete_subscriptions))
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


def subscribe(request):
    submitted = False
    if request.method == 'POST':
        form = SubscriptionForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/subscribe?submitted=True')
        else:
            print(form.errors)
    else:
        form = SubscriptionForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'subscribe.html', {'form':form, 'submitted':submitted, 'title':'Contact Me'})
