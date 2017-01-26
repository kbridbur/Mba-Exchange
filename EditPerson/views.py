from django.shortcuts import render
from django.http import HttpResponse, Http404
from AddPerson.models import Client, AddmissionsService, Service
from itertools import chain

def index(request, client_id):

    #ensure this client exists
    try:
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        raise Http404("There is no client with that ID")

    #retrieve both types of services they are recieving and combine
    services = Service.objects.filter(client__id = client_id)
    addmissions_services = AddmissionsService.objects.filter(client__id = client_id)
    all_services = list(chain(services, addmissions_services))

    #display
    return render(request, 'services.html', {'services':all_services})
