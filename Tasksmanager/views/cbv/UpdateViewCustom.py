from django.views.generic import UpdateView
from django.core.urlresolvers import reverse


class UpdateViewCustom(UpdateView):
    """
    here we define a base template for alll class based update view
    Thus most views are forced to extend this class
    Its worthy to note that the template name can also be changed
    """
    template_name = 'en/cbv/UpdateViewCustom.html'
    url_name=""
    # defines the name of the current url,helping to add
    #this link in the action attribute of the form

    def get_success_url(self):
        """
        overide the get success url by default
        :return:
        """
        return reverse(self.success_url)

    def get_context_data(self, **kwargs):
        """
        used to send data to the template defined in template_name
        :param kwargs:
        :return:
        """
        context = super(UpdateViewCustom, self).get_context_data(**kwargs)
        model_name = self.model._meta.verbose_name.title()
        #gets the verbose name property of the defined model

        context['model_name'] = model_name
        #sends verbose name property to the template
        context['url_name'] = self.url_name
        # sends name of url to template
        print(self.object.pk)
        return context

