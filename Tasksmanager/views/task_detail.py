from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Tasksmanager.models import Task
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

@login_required
def page(request, pk):
    check_task = Task.objects.filter(id=pk)


    try:
        task = check_task.get()
        #used to retrieve the record in queryset

    except(Task.DoesNotExist, Task.MultipleObjectsReturned):
        #allows the handling of two types of errors
        return HttpResponseRedirect(reverse('index'))
        #this line redirects the user if an exception is thrown.it could redirect to an error page

    else:
        request.session['last_task'] = task.id
        #records id porper in a session variable

    return render(request, 'en/public/task_detail.html', {'object': task})


