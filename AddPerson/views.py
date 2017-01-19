from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from AddPerson.forms import ClientForm, ConsultantForm, EditorForm, ProviderForm
from AddPerson.models import Client, Consultant, Editor, Provider

def index(request):
    return HttpResponse('Welcome')
    #some buttons that go to each of the different places

def add_client(request):
    ClientFormSet = modelformset_factory(Client, form = ClientForm)
    if request.method == 'POST':
        formset = ClientFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/Add/') #Where to redirect after the submit button is hit
    else:
        formset = ClientFormSet()
    return render(request, 'add_client.html', {'formset': formset})

def add_consultant(request):
    ConsultantFormSet = modelformset_factory(Consultant, form = ConsultantForm)
    if request.method == 'POST':
        formset = ConsultantFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/Add/') #Where to redirect after the submit button is hit
    else:
        formset = ConsultantFormSet()
    return render(request, 'add_client.html', {'formset': formset})

def add_editor(request):
    EditorFormSet = modelformset_factory(Editor, form = EditorForm)
    if request.method == 'POST':
        formset = EditorFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/Add/') #Where to redirect after the submit button is hit
    else:
        formset = EditorFormSet()
    return render(request, 'add_client.html', {'formset': formset})

def add_provider(request):
    ProviderFormSet = modelformset_factory(Provider, form = ProviderForm)
    if request.method == 'POST':
        formset = ProviderFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/Add/') #Where to redirect after the submit button is hit
    else:
        formset = ProviderFormSet()
    return render(request, 'add_client.html', {'formset': formset})
