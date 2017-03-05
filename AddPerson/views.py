from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.forms import modelform_factory
from AddPerson.forms import ClientForm, ConsultantForm, EditorForm, ProviderForm
from AddPerson.models import Client, Consultant, Editor, Provider

def index(request):
    urls = ['Client', 'Consultant', 'Editor', 'Provider']
    if 'Client' in request.POST:
        return HttpResponseRedirect('/add/client/')
    elif 'Consultant' in request.POST:
        return HttpResponseRedirect('/add/consultant/')
    elif 'Editor' in request.POST:
        return HttpResponseRedirect('/add/editor/')
    elif 'Provider' in request.POST:
        return HttpResponseRedirect('/add/provider/')
    return render(request, 'AddPerson/add_index.html', {'urls':urls})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if 'Submit another' in request.POST:
                return HttpResponseRedirect('/add/client/')
            elif 'Submit one' in request.POST:
                return HttpResponseRedirect('/add/') #Where to redirect after the submit button is hit
    else:
        form = ClientForm()
    return render(request, 'AddPerson/add_client.html', {'form': form, 'type': 'Add Client'})

def add_consultant(request):
    if request.method == 'POST':
        form = ConsultantForm(request.POST)
        if form.is_valid():
            form.save()
            if 'Submit another' in request.POST:
                return HttpResponseRedirect('/add/consultant/')
            elif 'Submit one' in request.POST:
                return HttpResponseRedirect('/add/') #Where to redirect after the submit button is hit
    else:
        form = ConsultantForm()
    return render(request, 'AddPerson/add_client.html', {'form': form, 'type': 'Add Consultant'})

def add_editor(request):
    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            form.save()
            if 'Submit another' in request.POST:
                return HttpResponseRedirect('/add/editor/')
            elif 'Submit one' in request.POST:
                return HttpResponseRedirect('/add/') #Where to redirect after the submit button is hit
    else:
        form = EditorForm()
    return render(request, 'AddPerson/add_client.html', {'form': form, 'type': 'Add Editor'})

def add_provider(request):
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            form.save()
            if 'Submit another' in request.POST:
                return HttpResponseRedirect('/add/provider/')
            elif 'Submit one' in request.POST:
                return HttpResponseRedirect('/add/') #Where to redirect after the submit button is hit
    else:
        form = ProviderForm()
    return render(request, 'AddPerson/add_client.html', {'form': form, 'type': 'Add Provider'})

def webvantaform(request):
    if request.is_ajax():
        if request.method == 'POST':
            json = request.body
    return HttpResponse("OK")
