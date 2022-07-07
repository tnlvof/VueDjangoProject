from .base import *


SECRET_KEY = 'django-insecure-^2prv=&h5vh3=t$2io(a_m70m@&@0=u0yr*4q#6j+^d9gv*a$3'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
