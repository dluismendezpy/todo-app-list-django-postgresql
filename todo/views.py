# Django
from django.http.request import HttpRequest
from django.shortcuts import render, redirect

# Owns
from .models import Todo

def todo_list(request):
    """ Return a list of task created """
    todo_data = Todo.objects.all()

    return render(request, 'todo/todo_list.html', {
        'todo_data' : todo_data
    })

def insert_todo(request:HttpRequest):
    """ Insert a new task """
    todo_to_insert = Todo(content = request.POST['task'])
    todo_to_insert.save()

    return redirect('todo_list')

def delete_todo(request, todo_id):
    """ Delete a task """
    todo_to_delete = Todo.objects.get(id = todo_id)
    todo_to_delete.delete()

    return redirect('todo_list')
