from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else: #if request.method == "GET"
        form = TaskForm()
    return render(request, 'create_or_edit_task.html', {'form':form, 'edit_mode':False})

def delete_task(request,task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_list')

def edit_task(request,task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance = task)
    return render(request, 'create_or_edit_task.html', {'form':form, 'edit_mode':True})
def task_list(request):
    tasks = Task.objects.all()
    return render(request,'task_list.html',{'tasks':tasks})

def task_detail(request,task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request,'task_detail.html',{'task':task})

