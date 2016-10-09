from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
		list_patient,
        new_patient,
        view_patient,
        edit_patient,
        delete_patient,
	)

urlpatterns = [
    url(r'^$', list_patient, name='list'),
    url(r'^new/$', new_patient, name='new'),
    url(r'^(?P<id>\d+)/', view_patient, name='view'),
    url(r'^edit/(?P<id>\d+)/$', edit_patient, name='edit'),
    url(r'^delete/(?P<id>\d+)/$', delete_patient, name='delete'),
]