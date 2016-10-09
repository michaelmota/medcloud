from django import forms

from .models import Patience
from .constants import insurancechoice,sexchoice,doctorchoice

class PatienceFilterForm(forms.Form):
	full_name 			= forms.CharField(label='Nombre Completo', required=False)
	phone				= forms.CharField(label='Telefono',required=False)
	cellphone			= forms.CharField(label='Celular',required=False)
	id_card_number		= forms.CharField(label='Cedula',required=False)
	insurancecompany	= forms.ChoiceField(label='Aseguradora', choices=insurancechoice, required=False)
	doctor				= forms.ChoiceField(label='Doctor', choices=doctorchoice, required=False)