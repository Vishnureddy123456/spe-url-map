from django.urls import path
from vishnu.views import *
app_name='Vishnu'
urlpatterns=[
    path('middle/',middle,name='middle'),
]