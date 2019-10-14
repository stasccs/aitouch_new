from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('create', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('single/<int:id>', views.single, name='single'),
    path('edit/<int:id>', views.edit, name='edit'),
]