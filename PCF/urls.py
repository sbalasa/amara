from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    # path("ajax_form", views.ajax_form, name="ajax_form"),
    # path("subscribe", views.index, name="subscribe")
    # path("ajax_sub", views.subscribe_ajax, name="ajax_sub")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)