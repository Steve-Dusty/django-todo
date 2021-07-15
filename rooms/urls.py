from django.urls import path, include
from .views import createRoom

urlpatterns = [

    path('createroom/', createRoom, name='createRoom'),

]
