from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings

from .forms import UserLoginForm
from citas.models import Cita
from patients.models import Patient
from records.models import Record

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

@login_required
def dashboard(request):
	citas_count = Cita.objects.count()
	patients_count = Patient.objects.count()
	records_count = Record.objects.count()

	context = {
		'citas_count':citas_count,
		'patients_count':patients_count,
		'records_count':records_count,
	}

	return render(request, "dashboard.html", context)


def logout_view(request):
	logout(request)
	messages.success(request, "Usted acaba de salir del sistema.")
	return HttpResponseRedirect(settings.LOGIN_URL)