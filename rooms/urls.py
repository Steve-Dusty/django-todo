from django.urls import path, include
from .views import createRoom, joinRoom

urlpatterns = [

    path('createroom/', createRoom, name='createRoom'),
    path('joinRoom/', joinRoom, name='joinRoom'),
]
