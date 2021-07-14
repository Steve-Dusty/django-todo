from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:room_code>', views.todoRoom, name='todoRoom'),
    path('createroom/', views.createRoom, name='createRoom'),

]
