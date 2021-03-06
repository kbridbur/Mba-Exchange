from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    urls = ['add', 'search']

    if 'add' in request.POST:
        return HttpResponseRedirect('/add/')
    elif 'search' in request.POST:
        return HttpResponseRedirect('/search/')
    return render(request, 'AddPerson/index.html', {'urls':urls})
