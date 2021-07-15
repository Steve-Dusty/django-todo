from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('room/<str:room_code>', views.todoPanel, name='panel'),
    path('room/<str:room_code>/addTask', views.addTask, name='addTask'),
    path('room/<str:room_code>/toggleTask/<int:task_id>',
         views.toggleTask, name='toggleTask'),
    path('room/<str:room_code>/deleteTask/<int:task_id>',
         views.deleteTask, name='deleteTask'),
    path('room/<str:room_code>/clearAll', views.clearAll, name='clearAll')
]
