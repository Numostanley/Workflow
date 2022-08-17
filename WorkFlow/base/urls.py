from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create-authomation', views.Create_Automation),
    path('opt-in', views.OptIn_EmailList),
    
    
]