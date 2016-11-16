# CORE
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
#MYAPPS
from .forms import RecordsCreateForm, RecordFilterForm
from .models import Record
from comments.forms import CommentForm
from comments.models import Comment
from records.models import Record
from patients.constants import doctorchoice
#3RDPARTY
from django_filters import FilterSet,CharFilter,NumberFilter,ChoiceFilter


class RecordFilter(FilterSet):
	paciente = CharFilter(name='paciente', lookup_type='icontains', distinct=True)
	doctor = ChoiceFilter(choices=doctorchoice,distinct=True)

	class Meta:
		model = Record
		fields = [
			"paciente",
			"doctor",
		]

@login_required
def list_record(request):
	records = Record.objects.all()
	# FILTER
	filterform = RecordFilterForm(data=request.GET or None)
	f = RecordFilter(request.GET, queryset=records)
	# PAGINATOR
	paginator = Paginator(records,10)
	page_request = "page"
	page = request.GET.get(page_request)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		"records":f,
		"filterform":filterform,
		"page_request":page_request,
		"object_list":queryset,
	}
	return render(request, "record_list.html", context)

def new_record(request):
	form = RecordsCreateForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form":form,
	}
	return render(request, "record_form.html", context)

@login_required
def view_record(request, id=None):
	instance = get_object_or_404(Record, id=id)
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
	return render(request, "record_view.html", context)

@login_required
def edit_record(request, id=None):
	instance = get_object_or_404(Record, id=id)
	form = RecordsCreateForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"instance":instance,
		"form":form,
	}
	return render(request, "record_form.html", context)

@login_required
def delete_record(request, id=None):
	instance = get_object_or_404(Record, id=id)
	instance.delete()
	messages.success(request, "El record %s se ha eliminado correctamente." %(instance.id))
	return redirect("records:list")