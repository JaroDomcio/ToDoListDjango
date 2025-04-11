
from django.urls import path
from .views import task_list, create_task, task_detail, delete_task

urlpatterns = [
    path('',task_list, name='task_list'),
    path('create_task',create_task, name='create_task'),
    path('task/<int:task_id>/',task_detail, name='task_detail'),
    path('task/delete/<int:task_id>/',delete_task, name='delete_task'),
]