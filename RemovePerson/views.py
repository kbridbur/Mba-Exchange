from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Remove someone from the database here!")
# Create your views here.
