from django.urls import path
from . import views

urlpatterns = [
    path('', views.newYear, name='newyear'),
]