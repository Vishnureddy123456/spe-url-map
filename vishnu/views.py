from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def middle(request):
    return HttpResponse('<h1><marquee>I have two brothers one is younger and another one is elder, who will always love me and taken care of me</h1></marquee>')