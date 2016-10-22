from django import forms

from .models import Cita
from patients.constants import insurancechoice,sexchoice,doctorchoice

class CitaFilterForm(forms.Form):
	paciente = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), label='Paciente', required=False)

class CitaCreateForm(forms.ModelForm):
	class Meta:
		model = Cita
		fields = [
			"date",
			"paciente",
			"doctor",
			"insurance",
			"observaciones",
			"diagnosis",
		]
		widgets = {
			"date": 		forms.TextInput(attrs={'class': 'form-control', 'placeholder':'AAAA-MM-DD'}),
			"paciente": 	forms.Select(attrs={'class': 'form-control'}),
			"doctor": 		forms.Select(attrs={'class': 'form-control'}),
			"insurance":	forms.Select(attrs={'class': 'form-control'}),
			"observaciones":forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),
			"diagnosis":	forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),
		}