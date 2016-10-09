from __future__ import unicode_literals

from django.db import models

from .constants import sexchoice,insurancechoice,doctorchoice

class Patient(models.Model):
	# PATIENCE DATA
	date 		= models.DateField()
	full_name 	= models.CharField(max_length=60)
	id_card_number = models.CharField(max_length=45)
	age 		= models.CharField(max_length=5, choices=sexchoice)
	birthdate	= models.DateField()
	address		= models.CharField(max_length=500)
	phone		= models.IntegerField()
	cellphone	= models.IntegerField()
	other_phone	= models.IntegerField()
	occupation	= models.CharField(max_length=45)
	position	= models.CharField(max_length=45)
	placeofwork	= models.CharField(max_length=45)
	work_phone	= models.IntegerField()
	insurancecompany 	= models.CharField(max_length=35, choices=insurancechoice)
	refered_by			= models.CharField(max_length=45)
	# EMERGENCY CONTACT
	in_case_of_emergency_contact 	= models.CharField(max_length=45)
	emergency_contact_phone 		= models.IntegerField()
	emergency_contact_cellphone 	= models.IntegerField()
	emergency_contact_othernum 		= models.IntegerField()
	# FORM FILLED BY
	form_filled_by 		= models.CharField(max_length=45)
	# DOCTOR
	doctor = models.CharField(max_length=45, choices=doctorchoice)

	def __unicode__(self):
		return self.full_name
