from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from AddPerson.models import Client, Consultant, Provider, Editor

def index(request):
    urls = ['Client', 'Consultant', 'Editor', 'Provider']
    if request.method == 'GET': # If the form is submitted

        #Get the queries from each of the possible search boxes
        consultant_query = request.GET.get('consultant_search', None)
        provider_query = request.GET.get('provider_search', None)
        editor_query = request.GET.get('editor_search', None)
        client_query = request.GET.get('client_search', None)
        print(request.GET)
        print(client_query)
        #check which was queried and search appropriately
        if (client_query != None):
            client_set = Client.FindClientsByName(client_query)
            if client_query == "":
                query = "All Clients"
            else:
                query = "clients by name of " + client_query
            return render(request, 'AddPerson/search_result.html', {'person_set':client_set, 'query': query})
        elif (consultant_query != None):
            consultant_set = Consultant.FindConsultantsByName(consultant_query)
            if consultant_query == "":
                query = "All Consultants"
            else:
                query = "consultants by name of " + consultant_query
            return render(request, 'AddPerson/search_result.html', {'person_set':consultant_set, 'query': query})
        elif (provider_query != None):
            provider_set = Provider.FindProvidersByName(provider_query)
            if provider_query == "":
                query = "All Providers"
            else:
                query = "providers by name of " + provider_query
            return render(request, 'AddPerson/search_result.html', {'person_set':provider_set, 'query': query})
        elif (editor_query != None):
            editor_set = Editor.FindEditorsByName(editor_query)
            if editor_query == "":
                query = "All Editors"
            else:
                query = "editors by name of " + editor_query
            return render(request, 'AddPerson/search_result.html', {'person_set':editor_set, 'query': query})
    return render(request, 'AddPerson/search_index.html', {'urls':urls, 'action':'search'})
