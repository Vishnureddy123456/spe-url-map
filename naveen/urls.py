from django.urls import path
from naveen.views import *
app_name='Naveen'
urlpatterns=[
    path('smaller/',smaller,name='smaller'),
]