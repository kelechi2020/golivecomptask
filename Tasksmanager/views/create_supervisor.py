from django.shortcuts import render
from Tasksmanager.models import Supervisor
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required()
def page(request):
    if request.POST:
        form = Form_supervisor(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            specialization = form.cleaned_data['specialization']
            email = form.cleaned_data['email']

            new_user = User.objects.create_user(username=login, email=email, password=password)
            # here we create an instance of the User model with the create_user() method

            new_user.is_active = True  # this is false by default to enable you create a system of account verification
            # by e mail or other means
            new_user.last_name = name

            new_user.save()

            new_supervisor = Supervisor(user_auth=new_user, specialization=specialization)
            # in above line we create a new supervisor with the form dataa
            new_supervisor.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'en/public/create_supervisor.html', {'form': form})
    else:
        form = Form_supervisor()
    return render(request, 'en/public/create_supervisor.html', {'form': form})



class Form_supervisor(forms.Form):
    name = forms.CharField(label="Name", max_length=30)
    login = forms.CharField(label='login')
    email = forms.EmailField(label='Email')
    specialization = forms.CharField(label='specialization')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_bis = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(Form_supervisor, self).clean()
        password = self.cleaned_data.get('passwword')
        password_bis = self.cleaned_data.get('passwword_bis')

        if password and password_bis and password != password_bis:
            raise forms.ValidationError('Passwords are not identical')
        return self.cleaned_data