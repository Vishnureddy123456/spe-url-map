from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bigger(request):
    return HttpResponse('<h1><marquee>I have two little brothers, who will always love me and taken care of me</h1></marquee>')
