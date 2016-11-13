# CORE
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
#MYAPPS
from .models import Cita
from .forms import CitaFilterForm,CitaCreateForm
from patients.constants import insurancechoice,doctorchoice
from comments.forms import CommentForm
from comments.models import Comment
#3RDPARTY
from django_filters import FilterSet,CharFilter,NumberFilter,ChoiceFilter,ModelChoiceFilter

# START VIEWS
class CitaFilter(FilterSet):
	paciente__patient = CharFilter(name='paciente', lookup_type='icontains', distinct=True)

	class Meta:
		model = Cita
		fields = [
			"paciente__patient",
		]

@login_required
def list_cita(request):
	citas = Cita.objects.all()
	filterform = CitaFilterForm(data=request.GET or None)
	f = CitaFilter(request.GET, queryset=citas)
	# PAGINATOR
	paginator = Paginator(citas, 20)
	page_request = "page"
	page = request.GET.get(page_request)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	# FORM
	form = CitaCreateForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Se ha creado con exito la llamada")
		return redirect("citas:list")

	context = {
		"form":form,
		"object_list":queryset,
		"citas":f,
		"page_request":page_request,
		"filterform":filterform,
	}

	return render(request, "cita_list.html", context)

@login_required
def view_cita(request, id=None):
	instance = get_object_or_404(Cita, id=id)
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
						content=content)
	comments = instance.comments
	# END COMMENT FORM
	context = {
		"instance":instance,
		"comments":comments,
		"comment_form":form,
	}
	return render(request, "cita_view.html", context)

@login_required
def edit_cita(request, id=None):
	instance = get_object_or_404(Cita, id=id)
	form = CitaCreateForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Se ha actualizado la terapia")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"instance":instance,
		"form":form,
	}
	return render(request, "cita_form.html", context)

@login_required
def delete_cita(request, id=None):
	instance = get_object_or_404(Cita, id=id)
	instance.delete()
	messages.success(request, "La Terapia %s se ha eliminado correctamente." %(instance.id))
	return redirect("citas:list")
