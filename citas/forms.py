from django import forms

from .models import Cita
from patients.constants import insurancechoice,sexchoice,doctorchoice

class CitaFilterForm(forms.Form):
	patient = forms.CharField(label='Nombre del Paciente', required=False)

class CitaCreateForm(forms.ModelForm):
	class Meta:
		model = Cita
		fields = [
			"patient",
		]