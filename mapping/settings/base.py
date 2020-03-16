"""
Base Django settings for factoryconcepts project.

THIS CONFIGURATION CANNOT NOT BE USED DIRECTLY.
Use development, staging, or production which inherit and override this.
"""
import os
from django.conf import global_settings

import dj_database_url
from getenv import env

from .pipeline import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# Secure by default, should only be overriden in development.py
DEBUG = False

# Retrieve configuration from environment
APP_ENV = env('APP_ENV', 'production')

# No default key to prevent running in staging/production
SECRET_KEY = env('SECRET_KEY')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


INSTALLED_APPS = (
    ### Django Modules
    'bootstrap_admin',  # must be before dj-admin
    # 'django.contrib.admin',
    'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django sites framework is required for `allauth`
    'django.contrib.sites',

    ### Vendor Modules
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_extensions',
    'pipeline',
    'rest_framework',
    'rest_framework_extensions',
    'rest_framework_swagger',

    ### Application Modules
    'mapping.accounts',
    'mapping.common',
    'mapping.frontend',
    'mapping.tagging',
)

# FAKER_LOCALE = None     # settings.LANGUAGE_CODE is loaded
# FAKER_PROVIDERS = None  # faker.DEFAULT_PROVIDERS is loaded (all)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mapping.common.middleware.GlobalUserMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',

                # Required by `allauth` template tags
                'django.template.context_processors.request'
            ]
        },
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

# Allauth authentication
# ACCOUNT_ADAPTER = 'mapping.accounts.adapter.CPMAccountAdapter'
ACCOUNT_SIGNUP_FORM_CLASS = 'mapping.accounts.forms.SignupForm'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# Email configuration
DEFAULT_FROM_EMAIL = 'Critical-Path Mapping <no-reply@criticalpathmapping.com>'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no-reply@criticalpathmapping.com'
EMAIL_HOST_PASSWORD = 'hwre7/q]~6Gng{~c0CkD{$_=z'
EMAIL_USE_TLS = True


BOOTSTRAP_ADMIN_SIDEBAR_MENU = False

ROOT_URLCONF = 'mapping.urls'

WSGI_APPLICATION = 'mapping.wsgi.application'

AUTH_USER_MODEL = 'accounts.User'

# Parse database configuration from DATABASE_URL environment variable
DATABASE_URL = env('DATABASE_URL')
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}


# Add bcrypt for super-duper security
PASSWORD_HASHERS = (
    'mapping.hashers.MyPBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
)



# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = False
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
MEDIA_ROOT = 'media'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'frontend', 'vendor'),
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, '..', 'bower_components'),
)

STATIC_ROOT = 'static_final'
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
    'pipeline.finders.CachedFileFinder',
)

# STATICFILES_STORAGE = 'mapping.storage.GZIPCachedStorage'
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'



REST_FRAMEWORK = {
    # Force numeric value to remain so
    'COERCE_DECIMAL_TO_STRING': False,

    'DEFAULT_PARSERS_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    # Only allow authenticated users access to API
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# # A sample logging configuration. The only tangible logging
# # performed by this configuration is to send an email to
# # the site admins on every HTTP 500 error when DEBUG=False.
# # See http://docs.djangoproject.com/en/dev/topics/logging for
# # more details on how to customize your logging configuration.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s' # noqa
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'mail_admins': {
#             'filters': ['require_debug_false'],
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             # 'handlers': ['null'],
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'tasks_info': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#     }
# }

# LOGIN_REDIRECT_URL = '/parts'
