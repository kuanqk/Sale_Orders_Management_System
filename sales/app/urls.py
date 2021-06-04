from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_app, name='index_app'),
]