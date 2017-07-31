from Tasksmanager.models import Project, Task, Supervisor, Developer
from django.shortcuts import render
from django.utils import timezone


def page(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'en/public/project_detail.html', {'project': project})



