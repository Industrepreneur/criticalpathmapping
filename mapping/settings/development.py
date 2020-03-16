"""
Settings overrides for local development.

NOT TO BE USED IN PRODUCTION UNDER ANY CIRCUMSTANCES
"""
from .base import *


DEBUG = True

# Allow all host headers
ALLOWED_HOSTS = ['*']

ADMINS = (
    ('Robin Bolton', 'robin@robinbolton.com'),
)


# Force Django Debug Toolbar visibility
def show_toolbar(request):
    if request.is_ajax():
        return False
    return True

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'mapping.settings.development.show_toolbar',
}

INSTALLED_APPS += (
    # 'debug_toolbar',
    # 'django_faker',
)

# Disable caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }}


# Django-extensions graph_models defaults
GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

PIPELINE_LIVE_SCRIPT_ARGUMENTS += '--map embedded '

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
