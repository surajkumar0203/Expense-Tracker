from django.urls import path
from myapp.views import home,delete_expence,ragistration,login_page,logout_page

urlpatterns = [
    path('',login_page,name="login"),
    path('home/',home,name="home"),
    path('ragister/',ragistration,name="ragister"),
    path('logout/',logout_page,name="logout_page"),

    path('delete_expence/<uuid>/',delete_expence,name='delete'),
   
]