from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.db import models

from comments.models import Comment
from patients.models import Patient
from patients.constants import doctorchoice,insurancechoice

class Cita(models.Model):
	# DATOS GENERALES
	date = models.DateField()
	paciente = models.ForeignKey(Patient, related_name='nombre_paciente')
	doctor = models.CharField(max_length=30, choices=doctorchoice)
	insurance = models.CharField(max_length=40, choices=insurancechoice)
	# DATOS DE LA CITA
	observaciones = models.CharField(max_length=500)
	diagnosis = models.TextField(max_length=500)
	# CREATED
	timestamp = models.DateField(auto_now_add=True,auto_now=False)

	def get_absolute_url(self):
		return reverse("citas:view", kwargs={"id": self.id})

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