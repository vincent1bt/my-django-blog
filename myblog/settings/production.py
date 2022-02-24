import os
from myblog.settings.common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

IP = os.environ['SERVER_IP']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = [IP]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/dj.cnf',
        },
    }
}

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_production')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}