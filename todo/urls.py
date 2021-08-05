# Django
from django.urls import path

# Owns
from . import views

urlpatterns = [
    path('list/', views.todo_list, name='todo_list'),
]
