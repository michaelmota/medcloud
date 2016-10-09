from django import forms

from .models import Patient
from .constants import insurancechoice,sexchoice,doctorchoice

class PatientFilterForm(forms.Form):
	full_name 			= forms.CharField(label='Nombre Completo', required=False)
	phone				= forms.CharField(label='Telefono',required=False)
	cellphone			= forms.CharField(label='Celular',required=False)
	id_card_number		= forms.CharField(label='Cedula',required=False)
	insurancecompany	= forms.ChoiceField(label='Aseguradora', choices=insurancechoice, required=False)
	doctor				= forms.ChoiceField(label='Doctor', choices=doctorchoice, required=False)

class PatientCreateForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = [
			"full_name",
			"id_card_number",
			"age",
			"birthdate",
			"address",
			"phone",
			"cellphone",
			"other_phone",
			"occupation",
			"position",
			"placeofwork",
			"work_phone",
			"insurancecompany",
			"refered_by",
			"in_case_of_emergency_contact",
			"emergency_contact_phone",
			"emergency_contact_cellphone",
			"emergency_contact_othernum",
			"form_filled_by",
			"doctor",
		]