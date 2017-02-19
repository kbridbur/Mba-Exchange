from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^client/', views.add_client, name='add_client'),
    url(r'^consultant/', views.add_consultant, name='add_consultant'),
    url(r'^editor/', views.add_editor, name='add_editor'),
    url(r'^provider/', views.add_provider, name='add_provider'),
]
