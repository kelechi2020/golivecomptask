from django.views.generic import DetailView
from Tasksmanager.models import Developer, Task


class Developer_detail(DetailView):
    model = Developer
    template_name = 'en/public/developer_detail.html'
    def get_context_data(self, **kwargs):
        # this overides the get_context_data() method

        context = super(Developer_detail, self).get_context_data(**kwargs)
        print(type(context))
        #this allows calling the method of the super class. Without this line
        # we would not have the basic context

        tasks_dev = Task.objects.filter(developers = self.object)
        print(type(tasks_dev))
        # This allows us to retrieve the list of developer task.we use self.object,
        #which is a developer type object already defined by the DetailView class

        context['tasks_dev'] = tasks_dev

        return context


