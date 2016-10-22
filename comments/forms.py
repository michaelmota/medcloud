from django import forms

from .models import Comment
from patients.constants import objetivochoice

class CommentForm(forms.Form):
	content_type = forms.CharField(widget=forms.HiddenInput)
	object_id = forms.IntegerField(widget=forms.HiddenInput)
	objetivo = forms.ChoiceField(widget=forms.Select(attrs={'class' : 'form-control'}),label='Motivo de la Visita', choices=objetivochoice)
	content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'rows':'4'}),label='Comentario')