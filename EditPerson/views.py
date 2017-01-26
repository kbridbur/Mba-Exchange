from django.shortcuts import render
from django.http import HttpResponse, Http404
from AddPerson.models import Client, AddmissionsService, Service
from itertools import chain
from AddPerson.forms import AddmissionsServiceForm, ServiceForm

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

    if request.method == 'POST':
        form1 = AddmissionsServiceForm(request.POST)
        form2 = ServiceForm(request.POST)
        if 'addmission' in request.POST:
            if form1.is_valid():
                form1.save()
        if 'service' in request.POST:
            if form2.is_valid():
                form2.save()
    else:
        form1 = AddmissionsServiceForm()
        form2 = ServiceForm()

    #display
    return render(request, 'services.html', {'services':all_services, 'form1':form1, 'form2':form2})
