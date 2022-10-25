from django.shortcuts import render
from .models import Project

# Create your views here.
def project_list(request):
    projects=Project.objects.all()
    context = {
        "project_list": projects,
    }
    return render(request, "projects/list.html", context)
