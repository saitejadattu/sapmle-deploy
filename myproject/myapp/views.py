from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def getUser(request):
    return HttpResponse("sample deploy")