from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponse("Add someone to the database here!")
# Create your views here.
