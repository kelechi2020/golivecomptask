from django.views.generic import CreateView, DetailView

from Tasksmanager.models import Task

class Task_list(DetailView):
    template_name = "en/public/task_detail.html"
    model = Task
    paginate_by = 5


