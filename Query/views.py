from django.shortcuts import render
from django.http import HttpResponse
from AddPerson.models import Client

def index(request):
    return HttpResponse("Search the database here!")
# Create your views here.
def client_search(request):
    ''' This could be your actual view or a new one '''
    # Your code
    if request.method == 'GET': # If the form is submitted

        search_query = request.GET.get('search_box', None)
        if (search_query != None):
            client_set = Client.FindClientsByName(search_query)
            if search_query == "":
                query = "All Clients"
            else:
                query = search_query
            return render(request, 'client_search_result.html', {'client_set':client_set, 'query': query})
    return render(request, 'search.html')
