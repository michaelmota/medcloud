from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings

from .forms import UserLoginForm

def login_view(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		return HttpResponseRedirect(reverse('dashboard'))
	
	context = {
		"form":form,
	}

	return render(request, 'login.html', context)

def dashboard(request):
	context = {

	}

	return render(request, "dashboard.html", context)


def logout_view(request):
	logout(request)
	messages.success(request, "Usted acaba de salir del sistema.")
	return HttpResponseRedirect(settings.LOGIN_URL)