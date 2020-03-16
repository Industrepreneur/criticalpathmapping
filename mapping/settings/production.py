"""
Settings overrides for production server.
"""
from .base import *

# Let's be paranoid, just to be safe...
DEBUG = False

# Specify allowed hosts
ALLOWED_HOSTS = [
    'criticalpathmapping.com',
    '.criticalpathmapping.com',
    '.mapping.mymanufacturing.org'
]

INSTALLED_APPS += (
    'gunicorn',
)

# Allauth authentication
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
