from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# file that takes requests and returns responses

def say_hello(request):
    x = 1
    y = 2
    return HttpResponse('Hello World - from CRS')