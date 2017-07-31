from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Tasksmanager.models import Task
from django.core.urlresolvers import reverse

@login_required
def page(request):
    tasks_list = Task.objects.all()
    # This line is used to retrieve all existing tasks database.


    return render(request, 'en/public/task_list.html', {'tasks_list': tasks_list})
