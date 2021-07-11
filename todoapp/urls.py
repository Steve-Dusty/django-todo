from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index, name='home'),
    path('panel/', views.todoPanel, name='panel'),
    path('addTask', views.addTask, name='addTask'),
    path('toggleTask/<int:task_id>', views.toggleTask, name='toggleTask'),
    path('deleteTask/<int:task_id>', views.deleteTask, name='deleteTask'),
    path('clearAll', views.clearAll, name='clearAll')
]