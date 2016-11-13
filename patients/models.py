from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

from .constants import sexchoice,insurancechoice,doctorchoice
from comments.models import Comment
class Patient(models.Model):
	# INFORMACION PRINCIPAL
	full_name 			= models.CharField(max_length=60)
	id_card_number 		= models.CharField(max_length=45)
	sex 				= models.CharField(max_length=10, choices=sexchoice)
	age					= models.CharField(max_length=3)
	birthdate			= models.DateField()
	refered_by			= models.CharField(max_length=45, blank=True,null=True)
	insurancecompany 	= models.CharField(max_length=35, choices=insurancechoice)
	# INFORMACION DE CONTACTO
	address				= models.CharField(max_length=500)
	phone				= models.IntegerField()
	cellphone			= models.IntegerField()
	other_phone			= models.IntegerField()
	# INFORMACION LABORAL
	occupation			= models.CharField(max_length=45)
	placeofwork			= models.CharField(max_length=45)
	position			= models.CharField(max_length=45)
	work_phone			= models.IntegerField()
	# CONTACTO DE EMERGENCIA
	in_case_of_emergency_contact 	= models.CharField(max_length=45)
	emergency_contact_phone 		= models.IntegerField()
	emergency_contact_cellphone 	= models.IntegerField()
	emergency_contact_othernum 		= models.IntegerField()
	# HISTORIA MEDICA
	doctor 					= models.CharField(max_length=45, choices=doctorchoice)
	antecedentes_personales	= models.TextField(max_length=500,null=True,blank=True)
	antecedentes_familiares = models.TextField(max_length=500,null=True,blank=True)
	enfermedad_actual		= models.TextField(max_length=500,null=True,blank=True)
	signos_sintomas			= models.TextField(max_length=500,null=True,blank=True)
	rehab_diagnosis			= models.CharField(max_length=500,null=True,blank=True)
	protocol_treatment		= models.CharField(max_length=500,null=True,blank=True)
	form_filled_by 			= models.CharField(max_length=45, blank=True,null=True)
	# faltante
	date 				= models.DateField(blank=True,null=True)
	timestamp 			= models.DateField(auto_now_add=True,auto_now=False)

	def __unicode__(self):
		return self.full_name

	def get_absolute_url(self):
		return reverse("pacientes:view", kwargs={"id": self.id})

	class Meta:
		ordering = ["-timestamp"]

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