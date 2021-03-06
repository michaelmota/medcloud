# CORE
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
#MYAPPS
from .models import Patient
from .constants import insurancechoice,doctorchoice
from .forms import PatientFilterForm, PatientCreateForm
from comments.forms import CommentForm
from comments.models import Comment
from records.models import Record
#3RDPARTY
from django_filters import FilterSet,CharFilter,NumberFilter,ChoiceFilter

# START VIEWS
class PatientFilter(FilterSet):
	full_name			= CharFilter(name='full_name', lookup_type='icontains', distinct=True)
	phone				= CharFilter(name='phone', lookup_type='icontains', distinct=True)
	cellphone			= CharFilter(name='cellphone', lookup_type='icontains', distinct=True)
	id_card_number		= CharFilter(name='id_card_number', lookup_type='icontains', distinct=True)
	insurancecompany	= ChoiceFilter(choices=insurancechoice,distinct=True)
	doctor 				= ChoiceFilter(choices=doctorchoice,distinct=True)

	class Meta:
		model = Patient
		fields = [
			"full_name",
			"phone",
			"cellphone",
			"id_card_number",
			"insurancecompany",
			"doctor",
		]

@login_required
def list_patient(request):
	pacientes = Patient.objects.all()
	# FILTER
	filterform = PatientFilterForm(data=request.GET or None)
	f = PatientFilter(request.GET, queryset=pacientes)
	# PAGINATOR
	paginator = Paginator(pacientes,10)
	page_request = "page"
	page = request.GET.get(page_request)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		"pacientes":f,
		"filterform":filterform,
		"page_request":page_request,
		"object_list":queryset,
	}
	return render(request, "paciente_list.html", context)

@login_required
def new_patient(request):
	form = PatientCreateForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form":form,
	}
	return render(request, "paciente_form.html", context)

@login_required
def view_patient(request, id=None):
	instance = get_object_or_404(Patient, id=id)
	# COMMENT FORM
	initial_data = {
		"content_type":instance.get_content_type,
		"object_id":instance.id,
	}
	form = CommentForm(request.POST or None, initial=initial_data)
	if form.is_valid():
		c_type = form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get("object_id")
		objetivo = form.cleaned_data.get("objetivo")
		content = form.cleaned_data.get("content")
		new_comment, created = Comment.objects.get_or_create(
						usuario=request.user,
						content_type=content_type,
						object_id=obj_id,
						objetivo=objetivo,
						content=content)
	comments = instance.comments
	# END COMMENT FORM
	context = {
		"instance":instance,
		"comments":comments,
		"comment_form":form,
	}
	return render(request, "paciente_view.html", context)

@login_required
def edit_patient(request, id=None):
	instance = get_object_or_404(Patient, id=id)
	form = PatientCreateForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"instance":instance,
		"form":form,
	}
	return render(request, "paciente_form.html", context)

@login_required
def delete_patient(request, id=None):
	instance = get_object_or_404(Patient, id=id)
	instance.delete()
	messages.success(request, "El paciente %s se ha eliminado correctamente." %(instance.id))
	return redirect("patients:list")