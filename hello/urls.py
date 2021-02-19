from django.urls import path
from . import views

urlpatterns = [
    path('', views.templ, name='index'),
    path('<str:name>', views.greet, name='greet'),
]