from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('home')
def sobre(request):
    return HttpResponse('sobre')
def contact(request):
    return HttpResponse('contact')