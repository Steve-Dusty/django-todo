from django.shortcuts import render, redirect
from .forms import CodeForm, JoinRoomForm
from .models import Code
from todoapp.models import Todo
from django.contrib import messages


def createRoom(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)

        if form.is_valid():
            if Code.objects.filter(room_code=form.cleaned_data['room_code']).exists():
                form = CodeForm()
                messages.error(
                    request, 'Room code already exists. Choose a new one.')
                return render(request, 'createroom.html', {'form': form})
            code = Code(room_code=form.cleaned_data['room_code'])
            code.save()
            return redirect('/room/' + form.cleaned_data['room_code'])
    else:
        form = CodeForm()

    context = {'form': form}

    return render(request, 'createroom.html', context)


def joinRoom(request):
    if request.method == 'POST':
        form = JoinRoomForm(request.POST)

        if form.is_valid():
            if Code.objects.filter(room_code=form.cleaned_data['room_code']).exists():
                return redirect('/room/' + form.cleaned_data['room_code'])

            else:
                messages.error(
                    request, 'Room code does not exist.'
                )
                print(form.cleaned_data['room_code'])
                return redirect('/')

    else:
        return redirect('/')
