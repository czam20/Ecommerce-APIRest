
from .base import *
from .base import env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8o@c1p_b&qs&^pg4iz!se2a###idtr$#wgrin+%vo46nj52kzy'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

#Email
EMAIL_BACKEND = env(
    'DJANGO_DEFAULT_FROM_EMAIL',
    default='django.core.mail.backends.console.EmailBackend'
)
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025