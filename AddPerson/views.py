from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Add someone to the database here!")
# Create your views here.
