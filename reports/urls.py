from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='reports'),
    url(r'^consultant_roster/', views.consultantRoster, name='consultantRoster'),
    url(r'^client_roster/'), views.clientRoster, name='clientRoster'),
    url(r'^consultant_client_round', views.consultantClientRound, name='consultantClientRound'),
]
