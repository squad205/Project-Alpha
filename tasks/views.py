from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.author = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/create.html", context)


@login_required
def task_list(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "task_list": tasks,
    }
    return render(request, "tasks/mine.html", context)
