"""
Django settings for chf_dmp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3qhe_a7=zcvm88#)6lu9zq)m3mehhco3sdx*nb^4(^of0u&2)*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# setting up for sending emails at BYU
# EMAIL_HOST = 'gateway.byu.edu'
# EMAIL_PORT = 25
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'nmjohnso'
# EMAIL_HOST_PASSWORD = 'Nat3J0hn50n'

# settings for using gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'nate8etan@gmail.com'
EMAIL_HOST_PASSWORD = 'Nat3J0hn50n'
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# SESSION_SAVE_EVERY_REQUEST = True
PASSWORD_RESET_TIMEOUT_DAYS = 1
# DEFAULT_FROM_EMAIL = 'nate8etan@gmail.com'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mako_plus.controller',
    'homepage',
    'account',
    'catalog',
    'polymorphic',          # pip install django-polymorphic
    'password_reset',       # pip install django-password-reset
    # 'bootstrap3_datetime',
    'bootstrap3',           # pip install django-bootstrap3
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_mako_plus.controller.router.RequestInitMiddleware',
)

ROOT_URLCONF = 'chf_dmp.urls'

WSGI_APPLICATION = 'chf_dmp.wsgi.application'

AUTH_USER_MODEL = 'homepage.SiteUser'
# AUTHENTICATION_BACKENDS = ("django_python3_ldap.auth.LDAPBackend",)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'db_chf',  # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'postgres',
            'PASSWORD': 'Nat3J0hn50n',
            'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '5433',  # Set to empty string for default.
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

DEBUG_PROPAGATE_EXCEPTIONS = DEBUG  # never set this True on a live site
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django_mako_plus': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "..", "www", "static")
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # SECURITY WARNING: this next line must be commented out at deployment
    BASE_DIR,
)
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = 'catalog/media/'

###############################################################
###   Specific settings for the Django-Mako-Plus app

# identifies where the Mako template cache will be stored, relative to each app
DMP_TEMPLATES_CACHE_DIR = 'cached_templates'

# the default app and page to render in Mako when the url is too short
DMP_DEFAULT_PAGE = 'index'
DMP_DEFAULT_APP = 'homepage'

# these are included in every template by default - if you put your most-used libraries here, you won't have to import them exlicitly in templates
DMP_DEFAULT_TEMPLATE_IMPORTS = [
    'import os, os.path, re',
]

# whether to send the custom DMP signals -- set to False for a slight speed-up in router processing
# determines whether DMP will send its custom signals during the process
DMP_SIGNALS = True

# whether to minify using rjsmin, rcssmin during 1) collection of static files, and 2) on the fly as .jsm and .cssm files are rendered
# rjsmin and rcssmin are fast enough that doing it on the fly can be done without slowing requests down
DMP_MINIFY_JS_CSS = True

# see the DMP online tutorial for information about this setting
DMP_TEMPLATES_DIRS = [
    # os.path.join(BASE_DIR, 'base_app', 'templates'),
]
