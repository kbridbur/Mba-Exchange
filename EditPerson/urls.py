from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^client/(?P<client_id>[0-9]+)/$', views.edit_client, name = 'edit view'),
    url(r'^consultant/(?P<consultant_id>[0-9]+)/$', views.edit_consultant, name = 'edit view'),
    url(r'^editor/(?P<editor_id>[0-9]+)/$', views.edit_editor, name = 'edit view'),
    url(r'^provider/(?P<provider_id>[0-9]+)/$', views.edit_provider, name = 'edit view'),
]
