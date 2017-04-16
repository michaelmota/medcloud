from django import forms

from .models import Record

class RecordFilterForm(forms.Form):
	paciente = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), label='Paciente', required=False)
	doctor = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), label='Doctor', required=False)


class RecordsCreateForm(forms.ModelForm):
	class Meta:
		model = Record
		fields = [
			"paciente",
			"antecedentes_personales",
			"antecedentes_familiares",
			"enfermedad_actual",
			"signos_sintomas",
			"rehab_diagnosis",
			"meta_corto_plazo",
			"meta_largo_plazo",
			"form_filled_by",
			"doctor",
		]
		widgets = {
			"doctor":						forms.Select(attrs={'class':'form-control'}),
			"paciente":						forms.Select(attrs={'class':'form-control'}),
			"antecedentes_personales": 		forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
			"antecedentes_familiares": 		forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
			"enfermedad_actual":			forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
			"signos_sintomas": 				forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
			"rehab_diagnosis": 				forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
			"meta_corto_plazo": 			forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
			"meta_largo_plazo": 			forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
			"form_filled_by": 				forms.TextInput(attrs={'class': 'form-control'}),
		}