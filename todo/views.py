# Django
from django.http.request import HttpRequest
from django.shortcuts import render, redirect

# Owns
from .models import Todo

def todo_list(request):
    todo_data = Todo.objects.all()

    return render(request, 'todo/todo_list.html', {
        'todo_data' : todo_data
    })

def insert_todo(request:HttpRequest):
    todo = Todo(content = request.POST['task'])
    todo.save()

    return redirect('todo_list')
