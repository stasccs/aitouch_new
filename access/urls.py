from django.urls import path
from . import views


urlpatterns = [
    path('reg', views.reg, name='reg'),
    path('entry', views.entry, name='entry'),
    path('exit_', views.exit_, name='exit_'),
    path('profile', views.profile, name='profile'),
    path('ajax1', views.ajax1, name='ajax1'),
]