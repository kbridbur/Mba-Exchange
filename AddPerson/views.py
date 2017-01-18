from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from AddPerson.forms import AddClientForm

def index(request):
    return HttpResponse("Add someone to the database here!")
# Create your views here.
def makeClient(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)

        if form.is_valid():
            HttpResponseRedirect('/')

    else:
        form = AddClientForm()

    return render(request, 'addclient.html', {'form':form}, content_type = 'application/xhtml+xml')
