# Django
from os import name
from django.urls import path

# Owns
from . import views

urlpatterns = [
    path('list/', views.todo_list, name='todo_list'),
    path('insert_todo/', views.insert_todo, name='insert_todo'),
    path('delete_todo/<int:todo_id>', views.delete_todo, name='delete_todo'),
]
