"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
#STATIC_URL = '/templates/'

BASE_DIR = Path(__file__).resolve().parent.parent

#STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATIC_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_DIRS = [
#     STATIC_DIR
#  ]
#LOCALE_PATHS = (
#   os.path.join(BASE_DIR, 'locale'),
#)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True
SESSION_COOKIE_DOMAIN = '.mativated.com'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

import mimetypes
mimetypes.add_type("text/css", ".css", True)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'h26.seohost.pl'
EMAIL_PORT = '587'
SERVER_EMAIL = 'no-reply@mativated.com'
EMAIL_HOST_USER = 'no-reply@mativated.com'
EMAIL_HOST_PASSWORD = 'kamorekxd1'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

try:
    env = os.environ["SECRET_KEY"]
    if env:
        SECRET_KEY = os.environ["SECRET_KEY"]
except:
    SECRET_KEY = 'django-insecure-q$h-7xe*!yo(u8wr-het-!8ybcp%wmyw-(mc+j^3(r7%&obof$'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = [
    "127.0.0.1",
    "mativated.com"
]
# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'cloudinary',
    'main',
    'Notifications',
    'Journal',
    'WorkoutJournal',
    'Clubs',
    'Presentation',
    'debug_toolbar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django.contrib.staticfiles',
    'account_register.apps.UsersConfig',
    # 'django.template.loaders.app_directories.load_template_source',
    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS' : True,
        'DIRS': [

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                # 'webp_converter.context_processors.webp_support',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Notifications.views.notifications',
                'Notifications.views.reportSuggestion'
            ],
        },
    },
]
AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

WSGI_APPLICATION = 'main.wsgi.application'
ASGI_APPLICATION = 'main.asgi.application'
# SESSIONS_ENGINE='django.contrib.sessions.backends.cache'
#


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = "/profile/"
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = None

# do zmiany True
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 7
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 500

import cloudinary
import cloudinary.uploader
import cloudinary.api
CLOUDINARY_STORAGE = {
  'CLOUD_NAME' : 'dj8dhfr6k',
  'API_KEY' : '676142837672146',
  'API_SECRET' : 'GmPJ0LooGJru061v4Q90na1b67o'
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'