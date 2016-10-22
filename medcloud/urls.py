from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import (
        dashboard,
        login_view,
        logout_view,
    )

urlpatterns = [
	# DASHBOARD
    url(r'^$', dashboard, name='dashboard'),
    url(r'^admin/', admin.site.urls),
    url(r'^citas/',include("citas.urls", namespace='citas')),
    url(r'^pacientes/',include("patients.urls", namespace='pacientes')),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)