from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Search the database here!")
# Create your views here.
