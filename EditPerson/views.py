from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
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

    if request.method == 'POST':
        form1 = AddmissionsServiceForm(request.POST)
        form2 = ServiceForm(request.POST)
        print(request.POST)
        if 'add_addmission' in request.POST:
            print('in')
            if form1.is_valid():
                preclient = form1.save(commit = False)
                preclient.client = client
                preclient.save()
                return HttpResponseRedirect('/edit/'+client_id+'/')
        if 'add_service' in request.POST:
            if form2.is_valid():
                preclient = form2.save(commit = False)
                preclient.client = client
                preclient.save()
                return HttpResponseRedirect('/edit/'+client_id+'/')
        delete_info = DeleteService(request.POST)
        print(delete_info)
        if delete_info[0] == 'addmissions':
            AddmissionsService.objects.get(pk=delete_info[1]).delete()
            print("delete addmissions service")
            return HttpResponseRedirect('/edit/'+client_id+'/')
        if delete_info[0] == 'service':
            Service.objects.get(pk=delete_info[1]).delete()
            print("delete service")
            return HttpResponseRedirect('/edit/'+client_id+'/')
    else:
        form1 = AddmissionsServiceForm()
        form2 = ServiceForm()

    #display the both forms
    return render(request, 'AddPerson/services.html', {'services':services, 'addmissions_services':addmissions_services, 'form1':form1, 'form2':form2})

def DeleteService(a):
    keys = a.dict().keys()
    for key in keys:
        words = key.split(" ")
        if 'service' in words:
            if 'addmissions' in words:
                print(words[-1])
                return ('addmissions', words[-1])
            return ('service', words[-1])
    return (None, None)
