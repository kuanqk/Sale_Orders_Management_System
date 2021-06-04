#from django.shortcuts import render

from django.http import HttpResponse

def index_app(request):
    return HttpResponse('Hello, you are in app index.')

