from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from AddPerson.forms import ClientForm
from AddPerson.models import Client

def add_client(request):
    ClientFormSet = modelformset_factory(Client, form = ClientForm)
    if request.method == 'POST':
        formset = ClientFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/admin/')
    else:
        formset = ClientFormSet()
    return render(request, 'add_client.html', {'formset': formset})
