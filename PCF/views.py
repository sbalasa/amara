import json

from .models import Subscriptions
from .forms import SubscriptionForm

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def index(request):
    complete_subscriptions = Subscriptions.objects.all()
    submitted = False
    form = SubscriptionForm()
    data  = {}
    if request.is_ajax:
        form = SubscriptionForm(request.POST or None)
        if form.is_valid():
            form.save()
            data['name'] = form.cleaned_data.get('name')
            data['subscription'] = form.cleaned_data.get('subscription')
            data['email'] = form.cleaned_data.get('email')
            return JsonResponse(data)
    return render(request, 'index.html', {'form':form, 'complete_subscriptions':complete_subscriptions})

# @csrf_protect
# def subscribe(request):
#     complete_subscriptions = Subscriptions.objects.all()
#     complete_subscriptions = json.loads(serializers.serialize("json", complete_subscriptions))
#     # print(complete_subscriptions[0]['fields'])
#     # complete_subscriptions = json.dumps(complete_subscriptions[0]['fields'])
#     # print(type(complete_subscriptions), complete_subscriptions)
#     # return JsonResponse(complete_subscriptions, safe=False)
#     return render(request, "subscribe.html", {"complete_subscriptions": complete_subscriptions})

# @csrf_protect
# def ajax_form(request):
#     # complete_subscriptions = Subscriptions.objects.all()
#     # complete_subscriptions = json.loads(serializers.serialize("json", complete_subscriptions))
#     if request.method == "POST":
#         ajax_data = json.loads(request.body)
#         name = ajax_data.get("name", None)
#         email = ajax_data.get("email", None)
#         subscriptions = ajax_data.get("subscriptions", None)
#         if name and email and subscriptions:
#             subscriptions_model = Subscriptions(
#                 name=name,
#                 email=email,
#                 subscriptions=subscriptions
#             )
#             subscriptions_model.save()
#             return HttpResponse(
#                 json.dumps({
#                     "name": name,
#                     "email": email,
#                     "subscriptions": subscriptions
#                 }),
#                 content_type='application/json'
#             )


