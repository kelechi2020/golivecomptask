from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, login

from django.shortcuts import render
from django.http import HttpResponse



class Form_login(forms.Form):
    email = forms.CharField()
    password = forms.CharField()


def page(request):
	if request.POST:
	# This line is used to check if the Form_connection form has been posted. If mailed, the form will be treated, otherwise it will be displayed to the user.
		form = Form_login(request.POST)
		if form.is_valid():
			username = form.cleaned_data["email"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)
			# This line verifies that the username exists and the password is correct.
			if user:
				# In this line, the authenticate function returns None if authentication has failed, otherwise it returns an object that validate the condition.
				login(request, user)
				# In this line, the login() function allows the user to connect.
				if request.GET.get('next') is not None:
					return redirect(request.GET['next'])

		else:
			return render(request, 'en/public/connection.html', {'form' : form})
	else:
		form = Form_login()
	return render(request, 'en/public/connection.html', {'form' : form})

""""
def page(request):

    error = False
# If form has posted
    if request.POST:
    # This line checks if the data was sent in POST. If so, this means that the form has been submitted and we should treat it.

        if 'logi' in request.POST:
            logi = request.POST.get('login', '')
        else:
            error = True
        if 'password' in request.POST:
            password = request.POST.get('password', '')
        else:
            error = True

        if not error:
            # We must get the supervisor
            user = authenticate(username=logi, password=password)
            # this line verifies whether user exists and password is correct

            if user:
                # authenticate returns none if it fails otherwise it returns a value that validates the condition
                login(request, user)
                # login function allows user to connect
                if request.GET.get('next') is not None:
                    return redirect(request.GET['next'])
        else:
            return HttpResponse("An error as occured")
    else:
        return render(request, 'en/public/connection.html')

"""