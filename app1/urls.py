from app1.views import *
from django.urls import path
app_name='yasmeen'
urlpatterns=[
    path('rizzu/',rizzu,name='rizzu'),
    path('shahida/',shahida,name='shahida'),
]