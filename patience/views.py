# CORE
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
#MYAPPS
from .models import Patience
from .constants import insurancechoice,doctorchoice
#3RDPARTY
from django_filters import FilterSet,CharFilter,NumberFilter,ChoiceFilter

# START VIEWS
class PatienceFilter(FilterSet):
	full_name			= CharFilter(name='full_name', lookup_type='icontains', distinct=True)
	phone				= CharFilter(name='phone', lookup_type='icontains', distinct=True)
	cellphone			= CharFilter(name='cellphone', lookup_type='icontains', distinct=True)
	id_card_number		= CharFilter(name='id_card_number', lookup_type='icontains', distinct=True)
	insurancecompany	= ChoiceFilter(choices=insurancechoice,distinct=True)
	doctor 				= ChoiceFilter(choices=doctorchoice,distinct=True)

	class Meta:
		model = Patience
		fields = [
			"full_name",
			"phone",
			"cellphone",
			"id_card_number",
			"insurancecompany",
			"doctor",
		]
