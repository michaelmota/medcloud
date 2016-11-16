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
	phone				= models.CharField(max_length=45)
	cellphone			= models.CharField(max_length=45,null=True,blank=True)
	other_phone			= models.CharField(max_length=45,null=True,blank=True)
	# INFORMACION LABORAL
	occupation			= models.CharField(max_length=45,null=True,blank=True)
	placeofwork			= models.CharField(max_length=45,null=True,blank=True)
	position			= models.CharField(max_length=45,null=True,blank=True)
	work_phone			= models.CharField(max_length=45,null=True,blank=True)
	# CONTACTO DE EMERGENCIA
	in_case_of_emergency_contact 	= models.CharField(max_length=45,null=True,blank=True)
	emergency_contact_phone 		= models.CharField(max_length=45,null=True,blank=True)
	emergency_contact_cellphone 	= models.CharField(max_length=45,null=True,blank=True)
	emergency_contact_othernum 		= models.CharField(max_length=45,null=True,blank=True)
	date 							= models.DateField(blank=True,null=True)
	timestamp 						= models.DateField(auto_now_add=True,auto_now=False)

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