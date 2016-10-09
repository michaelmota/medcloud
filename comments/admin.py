from django.contrib import admin
from django.apps import AppConfig

from .models import Comment
class ComentariosConfig(AppConfig):
    name = 'comentarios'

admin.site.register(Comment)