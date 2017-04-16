from django import forms

from .models import Patient
from .constants import insurancechoice,sexchoice,doctorchoice

class PatientFilterForm(forms.Form):
	full_name 			= forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), label='Nombre Completo', required=False)
	phone				= forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), label='Telefono',required=False)
	cellphone			= forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), label='Celular',required=False)
	id_card_number		= forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), label='Cedula',required=False)
	insurancecompany	= forms.ChoiceField(widget=forms.Select(attrs={'class' : 'form-control'}),label='Aseguradora', choices=insurancechoice, required=False)
	doctor				= forms.ChoiceField(widget=forms.Select(attrs={'class' : 'form-control'}),label='Doctor', choices=doctorchoice, required=False)


class PatientCreateForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = [
			"date",
			"full_name",
			"id_card_number",
			"sex",
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
		]
		widgets = {
			"date": 		forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"full_name": 	forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"id_card_number": forms.TextInput(attrs={'class': 'form-control input-circle', 'placeholder': 'Ej. 001-1111111-2'}),
			"sex": 			forms.Select(attrs={'class': 'form-control input-circle'}),
			"age": 			forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"birthdate": 	forms.TextInput(attrs={'class': 'form-control input-circle', 'placeholder': 'Ej. 1994-05-31 (AAAA-MM-DD)'}),
			"address": 		forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"phone":		forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"cellphone":	forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"other_phone": 	forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"occupation": 	forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"position": 	forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"placeofwork": 	forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"work_phone": 	forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"insurancecompany": 			forms.Select(attrs={'class': 'form-control input-circle',}),
			"refered_by": 					forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"in_case_of_emergency_contact": forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"emergency_contact_phone": 		forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"emergency_contact_cellphone": 	forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"emergency_contact_othernum": 	forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"form_filled_by": 				forms.TextInput(attrs={'class': 'form-control input-circle'}),
			"doctor": 						forms.Select(attrs={'class': 'form-control',}),
			"antecedentes_personales": 		forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
			"antecedentes_familiares": 		forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
			"enfermedad_actual":			forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
			"signos_sintomas": 				forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
			"rehab_diagnosis": 				forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
		}