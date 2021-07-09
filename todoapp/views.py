from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

def index(request):
    return render(request, 'home.html')


def todoPanel(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            task = Todo(task=form.cleaned_data['task'])
            task.save()
    else:
        form = TodoForm()
    
    data = Todo.objects.all()

    context =  {'form': form, 'tasks':data}

    return render(request, 'todo_panel.html', context)