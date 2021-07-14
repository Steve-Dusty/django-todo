from django.shortcuts import render, redirect
from .forms import CodeForm
from .models import Code
from django.contrib import messages


def createRoom(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)

        if form.is_valid():
            if Code.objects.filter(room_code=form.cleaned_data['room_code']).exists():
                form = CodeForm()
                messages.error(
                    request, 'Room code already exists. Choose a new one.')
                return render(request, 'rooms/createroom.html', {'form': form})
            code = Code(room_code=form.cleaned_data['room_code'])
            code.save()
            return redirect('/room/' + form.cleaned_data['room_code'])
    else:
        form = CodeForm()

    context = {'form': form}

    return render(request, 'rooms/createroom.html', context)


def todoRoom(request, room_code):
    codes = Code.objects.all()
    if Code.objects.filter(room_code=room_code).exists():
        context = {'codes': codes, 'room_code': room_code}
        return render(request, 'rooms/todolist.html', context)
    else:
        return redirect('/')
