from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
		list_record,
        new_record,
        view_record,
        edit_record,
        delete_record,
	)

urlpatterns = [
    url(r'^$', list_record, name='list'),
    url(r'^new/$', new_record, name='new'),
    url(r'^(?P<id>\d+)/', view_record, name='view'),
    url(r'^edit/(?P<id>\d+)/$', edit_record, name='edit'),
    url(r'^delete/(?P<id>\d+)/$', delete_record, name='delete'),
]