from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.contenttypes.models import ContentType
from patients.models import Patient
from patients.constants import doctorchoice
from comments.models import Comment

class Record(models.Model):
	paciente				= models.ForeignKey(Patient,null=True,blank=True)
	doctor 					= models.CharField(max_length=45, choices=doctorchoice,null=True,blank=True)
	antecedentes_personales	= models.TextField(max_length=500,null=True,blank=True)
	antecedentes_familiares = models.TextField(max_length=500,null=True,blank=True)
	enfermedad_actual		= models.TextField(max_length=500,null=True,blank=True)
	signos_sintomas			= models.TextField(max_length=500,null=True,blank=True)
	rehab_diagnosis			= models.TextField(max_length=500,null=True,blank=True)
	protocol_treatment		= models.TextField(max_length=500,null=True,blank=True)
	form_filled_by 			= models.TextField(max_length=45, blank=True,null=True)
	timestamp 				= models.DateField(auto_now_add=True,auto_now=False)

	def get_absolute_url(self):
		return reverse("records:view", kwargs={"id": self.id})

	@property
	def comments(self):
		instance = self
		qs = Comment.objects.filter_by_instance(instance)
		return qs

	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type