from .base import *

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.local.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



