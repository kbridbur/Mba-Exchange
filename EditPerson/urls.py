from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<client_id>[0-9]+)/$', views.index, name = 'edit view'),
]
