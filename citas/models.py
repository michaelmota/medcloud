from __future__ import unicode_literals

from django.db import models

from comments.models import Comment
from patients.models import Patient
from patients.constants import doctorchoice,insurancechoice

class Cita(models.Model):
	# DATOS GENERALES
	date = models.DateField()
	patient = models.ForeignKey(Patient)
	doctor = models.CharField(max_length=30, choices=doctorchoice)
	insurance = models.CharField(max_length=40, choices=insurancechoice)
	# DATOS DE LA CITA
	observaciones = models.CharField(max_length=500)
	diagnosis = models.TextField(max_length=500)
	# CREATED
	timestamp = models.DateField(auto_now_add=True,auto_now=False)

	def __unicode__(self):
		return self.patient