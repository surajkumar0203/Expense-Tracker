from django.urls import path
from myapp.views import home,delete_expence

urlpatterns = [
    path('',home,name="home"),
    path('delete_expence/<uuid>',delete_expence,name='delete'),
   
]