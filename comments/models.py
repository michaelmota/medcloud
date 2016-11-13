from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# IMPORTS
from patients.constants import objetivochoice
# MODELS
class CommentManager(models.Manager):
	def filter_by_instance(self,instance):
		content_type = ContentType.objects.get_for_model(instance.__class__)
		obj_id = instance.id
		queryset = super(CommentManager, self).filter(content_type=content_type,object_id=obj_id)
		return queryset

class Comment(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	#objetivo = models.CharField(max_length=40, choices=objetivochoice, blank=True,null=True)
	content = models.TextField(max_length=500)
	timestamp = models.DateField(auto_now_add=True,auto_now=False)

	objects = CommentManager()

	def __unicode__(self):
		return str(self.usuario.username)