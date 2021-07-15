from django.shortcuts import render, redirect
from .models import Todo
from rooms.models import Code
from .forms import TodoForm
from rooms.forms import CodeForm
from django.views.decorators.http import require_POST
from django.contrib import messages


def index(request):
    return render(request, 'home.html')


def todoPanel(request, room_code):
    codes = Code.objects.all()
    if Code.objects.filter(room_code=room_code).exists():
        context = {'codes': codes, 'room_code': room_code}

        form = TodoForm()

        # todo_list = Todo.objects.order_by('-id')
        todo_list = Todo.objects.filter(
            code=Code.objects.get(room_code=room_code)).order_by('-id')

        context = {'form': form, 'tasks': todo_list, 'room_code': room_code}
        return render(request, 'todo_panel.html', context)

    else:
        return redirect('/')


@require_POST
def addTask(request, room_code):
    if request.method == 'POST':

        form = TodoForm(request.POST)
        if form.is_valid():
            if Todo.objects.filter(code=(Code.objects.get(room_code=room_code)), task=form.cleaned_data['task']).exists() == False:
                task = Todo(
                    task=form.cleaned_data['task'], code=Code.objects.get(room_code=room_code))
                task.save()
            else:
                messages.error(request, 'Cannot add duplicate task')
                return redirect('panel', room_code=room_code)

        return redirect('panel', room_code=room_code)


def toggleTask(request, room_code, task_id):
    task = Todo.objects.get(pk=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('panel', room_code=room_code)


def deleteTask(request, room_code, task_id):
    task = Todo.objects.get(pk=task_id)
    task.delete()
    return redirect('panel', room_code=room_code)


def clearAll(request, room_code):

    Todo.objects.filter(code=Code.objects.get(room_code=room_code)).delete()

    return redirect('panel', room_code=room_code)
