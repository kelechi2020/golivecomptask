from django.views.generic import UpdateView
from Tasksmanager.models import Task
from django.forms import ModelForm
from django.core.urlresolvers import reverse

class Form_task_time(ModelForm):
    #create a form that extends the model form.
    # the updateview and createview cbv are based on a model form system
    class Meta:
        model = Task
        fields = ['time_elasped']
        #this defines the field that appear in the form

class Task_update_time(UpdateView):
    model = Task
    template_name = "en/public/update_task_developer.html"
    form_class = Form_task_time
#here we force the cbv to use the model form we created

    success_url = "index"
    #this sets the name of the url that will be seen once
    #  change is completed
    def get_success_url(self):
    # the line overrides and adds to the success_url method of the updateview class
        #the reverse method returns the URL corresponding to a url name
        return reverse(self.success_url)
