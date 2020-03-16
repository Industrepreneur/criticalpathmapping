from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework_swagger.views import get_swagger_view

from mapping.admin import manager_admin, site_admin
from mapping.accounts.views import LoginView, LogoutView

admin.autodiscover()

schema_view = get_swagger_view(title='Critical-Path Mapping API')

urlpatterns = [
    # API Endpoints
    url(r'^api/v1/', include('mapping.accounts.urls')),
    url(r'^api/v1/', include('mapping.tagging.urls')),
    url(r'^api/v1/auth/login', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout', LogoutView.as_view(), name='logout'),

    # Swagger API documentation
    # url(r'^docs/', schema_view),

    url(r'^accounts/', include('allauth.urls')),

    # Group Administration
    url(r'^admin/', include(manager_admin.urls), name='manageradmin'),
    url(r'^admin$', RedirectView.as_view(url='admin/', permanent=True), name='manageradmin'),

    # Super Administration
    url(r'^backend/', include(site_admin.urls), name='siteadmin'),
    url(r'^backend$', RedirectView.as_view(url='backend/', permanent=True), name='siteadmin'),

    # Main frontend interface
    url(r'^', include('mapping.frontend.urls')),
]
