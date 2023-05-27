from django.urls import path
from prasad.views import *
app_name='Prasad'
urlpatterns=[
    path('bigger/',bigger,name='bigger'),
]