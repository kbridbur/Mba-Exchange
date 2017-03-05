from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from AddPerson.models import Client, AddmissionsService, Service, Editor, Consultant, Provider
from itertools import chain
from AddPerson.forms import AddmissionsServiceForm, ServiceForm

def edit_client(request, client_id):

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
        if 'add_addmission' in request.POST:
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
        if delete_info[0] == 'addmissions':
            AddmissionsService.objects.get(pk=delete_info[1]).delete()
            return HttpResponseRedirect('/edit/'+client_id+'/')
        if delete_info[0] == 'service':
            Service.objects.get(pk=delete_info[1]).delete()
            return HttpResponseRedirect('/edit/'+client_id+'/')
    else:
        form1 = AddmissionsServiceForm()
        form2 = ServiceForm()

    #display the both forms
    return render(request, 'AddPerson/services.html', {'services':services, 'addmissions_services':addmissions_services, 'form1':form1, 'form2':form2, "client_display":client.GetDisplayFields()})

def edit_consultant(request, consultant_id):

    #ensure this client exists
    try:
        consultant = Consultant.objects.get(pk=consultant_id)
    except Consultant.DoesNotExist:
        raise Http404("There is no client with that ID")

    #retrieve clients
    clients = Client.objects.filter(consultant__id = consultant_id)

    #display
    return render(request, 'AddPerson/non_client_search_result.html', {"person_type": "consultant", "first_name":consultant.first_name, 'last_name':consultant.last_name, 'related_person_type': 'client', 'person_set': clients})

def edit_provider(request, provider_id):

    #ensure this client exists
    try:
        provider = Provider.objects.get(pk=provider_id)
    except Provider.DoesNotExist:
        raise Http404("There is no client with that ID")

    #retrieve clients
    clients = Client.objects.filter(provider__id = provider_id)

    #display
    return render(request, 'AddPerson/non_client_search_result.html', {"person_type": "provider", "first_name":provider.first_name, 'last_name':provider.last_name, 'related_person_type': 'client', 'person_set': clients})

def edit_editor(request, editor_id):

    #ensure this client exists
    try:
        editor = Editor.objects.get(pk=editor_id)
    except Editor.DoesNotExist:
        raise Http404("There is no client with that ID")

    #retrieve clients
    consultants = Consultant.objects.filter(editor__id = editor_id)

    #display
    return render(request, 'AddPerson/non_client_search_result.html', {"person_type": "editor", "first_name":editor.first_name, 'last_name':editor.last_name, 'related_person_type': 'consultant', 'person_set': consultants})

'''
@param a QueryDict of a post request
Look through a post request and find ids of objects to be deleted
@return a tuple of instruction and item to execute that instruction upon, tuple of Nones should there be nothing to do.
'''
def DeleteService(a):
    keys = a.dict().keys()
    for key in keys:
        words = key.split(" ")
        if 'service' in words:
            if 'addmissions' in words:
                return ('addmissions', words[-1])
            return ('service', words[-1])
    return (None, None)
