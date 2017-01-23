from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from AddPerson.models import Client, Consultant, Provider, Editor

def index(request):
    urls = ['Client', 'Consultant', 'Editor', 'Provider']
    if 'Client' in request.POST:
        return HttpResponseRedirect('/Search/search clients/')
    elif 'Consultant' in request.POST:
        return HttpResponseRedirect('/Search/search consultants/')
    elif 'Editor' in request.POST:
        return HttpResponseRedirect('/Search/search editors/')
    elif 'Provider' in request.POST:
        return HttpResponseRedirect('/Search/search providers/')
    return render(request, 'index_page.html', {'urls':urls, 'action':'search'})

# Create your views here.
def client_search(request):
    if request.method == 'GET': # If the form is submitted

        search_query = request.GET.get('search_box', None)
        if (search_query != None):
            client_set = Client.FindClientsByName(search_query)
            if search_query == "":
                query = "All Clients"
            else:
                query = "clients by name of " + search_query
            return render(request, 'search_result.html', {'person_set':client_set, 'query': query})
    return render(request, 'search.html')

def consultant_search(request):
    if request.method == 'GET': # If the form is submitted

        search_query = request.GET.get('search_box', None)
        if (search_query != None):
            consultant_set = Consultant.FindConsultantsByName(search_query)
            if search_query == "":
                query = "All Consultants"
            else:
                query = "consultants by name of " + search_query
            return render(request, 'search_result.html', {'person_set':consultant_set, 'query': query})
    return render(request, 'search.html')

def provider_search(request):
    if request.method == 'GET': # If the form is submitted

        search_query = request.GET.get('search_box', None)
        if (search_query != None):
            provider_set = Provider.FindProvidersByName(search_query)
            if search_query == "":
                query = "All Providers"
            else:
                query = "providers by name of " + search_query
            return render(request, 'search_result.html', {'person_set':provider_set, 'query': query})
    return render(request, 'search.html')

def editor_search(request):
    if request.method == 'GET': # If the form is submitted

        search_query = request.GET.get('search_box', None)
        if (search_query != None):
            editor_set = Editor.FindEditorsByName(search_query)
            if search_query == "":
                query = "All Editors"
            else:
                query = "editors by name of " + search_query
            return render(request, 'search_result.html', {'person_set':editor_set, 'query': query})
    return render(request, 'search.html')
