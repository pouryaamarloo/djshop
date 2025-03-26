from .common import *
INSTALLED_APPS = [
    'daphne',
    'drf_spectacular',
] + INSTALLED_APPS

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djshop',
        'USER': 'djshop',
        'PASSWORD': '123@456',
        'HOST': 'db',
        'PORT': '5432',
    }
}