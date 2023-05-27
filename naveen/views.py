from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def smaller(request):
    return HttpResponse('<marquee><h1>I have two big brothers, who will always love me and taken care of me</h1></marquee>')
