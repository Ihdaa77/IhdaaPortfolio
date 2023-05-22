from . import views
from django.urls import path

urlpatterns = [
    path('App', views.App, name='App'),
    path('Website', views.Website, name='Website'),
    path('System', views.System, name='System'),
]