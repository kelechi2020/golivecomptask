from Tasksmanager.models import Task
from django.core.urlresolvers import reverse
from django.views.generic import DeleteView


class Task_delete(DeleteView):
    model = Task
    success_url = "index"
    template_name = "en/public/confirm_delete_task.html"

    def get_success_url(self):
        return reverse(self.success_url)
    def get_context_data(self, **kwargs):
        context = super(Task_delete, self).get_context_data(**kwargs)
        task_del = Task.objects.get(pk=self.object.id)
        #this line gets the details of the task about to be deleted form the task model
        #from the Task_delete class instance using pk = self.object.id and adds it to the context data sent to the
        # template for display

        context['task_del'] = task_del

        return context