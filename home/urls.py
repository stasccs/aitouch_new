from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('thanks', views.thanks, name='thanks'),

]