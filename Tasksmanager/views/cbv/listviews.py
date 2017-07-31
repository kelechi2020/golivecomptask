from django.views.generic.list import ListView

from Tasksmanager.models import Project

class Project_list(ListView):
    template_name = "en/public/project_list.html"
    model = Project

    paginate_by = 5

    def get_queryset(self):
        """
        here we overide the get query set method of the list view class
        """
        queryset = Project.objects.all().order_by("title")
        return queryset
