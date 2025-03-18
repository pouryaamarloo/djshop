from .common import *
INSTALLED_APPS = [
    'daphne',
    'drf_spectacular',
] + INSTALLED_APPS

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


