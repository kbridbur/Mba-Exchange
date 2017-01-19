from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.client_search, name='search'),
]
