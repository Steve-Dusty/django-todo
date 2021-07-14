from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST


def index(request):
    return render(request, 'todoapp/home.html')


def todoPanel(request):
    form = TodoForm()

    todo_list = Todo.objects.order_by('-id')

    context = {'form': form, 'tasks': todo_list}

    return render(request, 'todoapp/todo_panel.html', context)


@require_POST
def addTask(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            task = Todo(task=form.cleaned_data['task'])
            task.save()

        return redirect('panel')


def toggleTask(request, task_id):
    task = Todo.objects.get(pk=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('panel')


def deleteTask(request, task_id):
    task = Todo.objects.get(pk=task_id)
    task.delete()
    return redirect('panel')


def clearAll(request):
    Todo.objects.all().delete()

    return redirect('panel')
