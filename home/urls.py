from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("contact", views.contact, name='contact'), 
    
    path("apps", views.apps, name='apps'), 
    path("apps/calc", views.calc, name='calc'), 

    path("music", views.music, name='music'), 
    path("music/melancholy", views.melancholy, name='melancholy'), 
    path("music/recuerdos_1", views.recuerdos_1, name='recuerdos_1'), 
    path("music/recuerdos_2", views.recuerdos_2, name='recuerdos_2'), 
    path("music/recuerdos_3", views.recuerdos_3, name='recuerdos_3'),  


]