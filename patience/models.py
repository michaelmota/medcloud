from __future__ import unicode_literals

from django.db import models

from .constants import sexchoice,insurancechoice

class Patience(models.Model):
	# PATIENCE DATA
	date 		= models.DateField()
	name 		= models.CharField(max_length=45)
	last_name 	= models.CharField(max_length=45)
	age 		= models.CharField(max_length=5, choices=sexchoice)
	birthdate	= models.DateField()
	address		= models.CharField(max_length=500)
	phone		= models.IntegerField(max_digits=10)
	cellphone	= models.IntegerField(max_digits=10)
	other_phone	= models.IntegerField(max_digits=10)
	occupation	= models.CharField(max_length=45)
	position	= models.CharField(max_length=45)
	placeofwork	= models.CharField(max_length=45)
	work_phone	= models.IntegerField(max_digits=10)
	insurancecompany 	= models.CharField(max_length=35, choices=insurancechoice)
	refered_by			= models.CharField(max_length=45)
	# EMERGENCY CONTACT
	in_case_of_emergency_contact 	= models.CharField(max_length=45)
	emergency_contact_phone 		= models.IntegerField(max_digits=10)
	emergency_contact_cellphone 	= models.IntegerField(max_digits=10)
	emergency_contact_othernum 		= models.IntegerField(max_digits=10)
	# FORM FILLED BY
	form_filled_by 		= models.CharField(max_length=45)
	id_card_number 		= models.CharField(max_length=45)

