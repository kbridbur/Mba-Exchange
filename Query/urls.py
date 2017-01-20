from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='search'),
    url(r'^search clients', views.client_search, name='search'),
    url(r'^search consultants', views.consultant_search, name='search'),
    url(r'^search providers', views.provider_search, name='search'),
    url(r'^search editors', views.editor_search, name='search'),
]
