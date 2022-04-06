from django.urls import path
from . import views

urlpatterns = [
    path('home', views.showform, name='home'),
    path('automate', views.automate, name='automate'),

]
