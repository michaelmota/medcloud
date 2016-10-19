# CORE
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
#MYAPPS
from .models import Cita
from comments.forms import CommentForm
from comments.models import Comment
#3RDPARTY
from django_filters import FilterSet,CharFilter,NumberFilter,ChoiceFilter

# START VIEWS
# class CitaFilter(FilterSet):
# 	full_name			= CharFilter(name='full_name', lookup_type='icontains', distinct=True)
# 	phone				= CharFilter(name='phone', lookup_type='icontains', distinct=True)
# 	cellphone			= CharFilter(name='cellphone', lookup_type='icontains', distinct=True)
# 	id_card_number		= CharFilter(name='id_card_number', lookup_type='icontains', distinct=True)
# 	insurancecompany	= ChoiceFilter(choices=insurancechoice,distinct=True)
# 	doctor 				= ChoiceFilter(choices=doctorchoice,distinct=True)

# 	class Meta:
# 		model = Patient
# 		fields = [
# 			"full_name",
# 			"phone",
# 			"cellphone",
# 			"id_card_number",
# 			"insurancecompany",
# 			"doctor",
# 		]

def list_cita(request):
	citas = Patient.objects.all()
	# FILTER
	filterform = PatientFilterForm(data=request.GET or None)
	f = PatientFilter(request.GET, queryset=citas)
	# PAGINATOR
	paginator = Paginator(citas,10)
	page_request = "page"
	page = request.GET.get(page_request)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		"citas":f,
		"filterform":filterform,
		"page_request":page_request,
		"object_list":queryset,
	}
	return render(request, "cita_list.html", context)

def view_cita(request, id=None):
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

def edit_cita(request):
	return render(request, "cita_form.html", context)

def delete_cita(request):
	return redirect("citas:list")