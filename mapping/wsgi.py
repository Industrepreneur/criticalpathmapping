"""
WSGI config for factoryconcepts project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application

from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mapping.settings.production")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)


# import django.views.debug
#
#
# def null_technical_500_response(request, exc_type, exc_value, tb):
#     raise exc_type(exc_value).with_traceback(tb)
# django.views.debug.technical_500_response = null_technical_500_response
#
# from werkzeug.debug import DebuggedApplication
# application = DebuggedApplication(application, evalex=True)
