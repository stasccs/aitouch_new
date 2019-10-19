from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('smm', views.smm, name='smm'),
    path('seo', views.seo, name='seo'),
    path('email', views.email, name='email'),
    path('context', views.context, name='context'),
    path('thanks', views.thanks, name='thanks'),

]