from django import forms

from .models import Comment
from propiedades.constants import objetivochoice


class CommentForm(forms.Form):
	content_type = forms.CharField(widget=forms.HiddenInput)
	object_id = forms.IntegerField(widget=forms.HiddenInput)
	objetivo = forms.ChoiceField(label='Motivo de la Visita', choices=objetivochoice)
	content = forms.CharField(label='Comentario', widget=forms.Textarea)