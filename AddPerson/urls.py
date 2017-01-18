from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.add_client, name='add_client'),
]
