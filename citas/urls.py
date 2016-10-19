from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
		list_cita,
        view_cita,
        edit_cita,
        delete_cita,
	)

urlpatterns = [
    url(r'^$', list_cita, name='list'),
    #url(r'^new/$', new_patient, name='new'),
    url(r'^(?P<id>\d+)/', view_cita, name='view'),
    url(r'^edit/(?P<id>\d+)/$', edit_cita, name='edit'),
    url(r'^delete/(?P<id>\d+)/$', delete_cita, name='delete'),
]