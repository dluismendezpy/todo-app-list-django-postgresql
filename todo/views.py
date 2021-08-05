# Django
from django.shortcuts import render

# Owns
from .models import Todo

def todo_list(request):
    todo_data = Todo.objects.all()

    return render(request, 'todo/todo_list.html', {
        'todo_data' : todo_data
    })
