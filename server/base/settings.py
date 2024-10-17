"""
Django settings for usage_explorer project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from datetime import timedelta
import os
import environ
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Env vars
DATABASE            = os.environ.get('DATABASE', 'postgres')
DATABASE_NAME       = os.environ.get('DATABASE_NAME', 'base')
POSTGRES_HOST       = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_PORT       = os.environ.get('POSTGRES_PORT', 5432)
POSTGRES_USER       = os.environ.get('POSTGRES_USER', 'base')
POSTGRES_PASSWORD   = os.environ.get('POSTGRES_PASSWORD', 'development')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
DEV_KEY = "_6qt7&n^^7*414a!u$@6ivtnln*ybc3vyzt-ggzir2-@zo@8-("
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", DEV_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

if os.environ.get("DJANGO_ALLOWED_HOSTS"):
    ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(",")
else:
    ALLOWED_HOSTS = ["*"]

# Required for default site
SITE_ID=1

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sites",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "allauth",
    "allauth.account",
    "dj_rest_auth.registration",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.usersessions",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "django_filters",
    "app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATABASE_NAME,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
    }
}

DATABASES['default'] = DATABASES[DATABASE]

CACHES = {
    'main_sqlite': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    'main_postgres': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'MAIN_CACHE',
        'OPTIONS': {
            'MAX_ENTRIES': 10000
        }
    }
}

CACHES['default']   = CACHES['main_{}'.format(DATABASE)]


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
}

# Simple JWT Settings
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

LOGIN_REDIRECT_URL = '/'

FRONTEND_URL = os.environ.get("FRONTEND_URL", "http://localhost:3000")
BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")

CORS_ORIGIN_WHITELIST = [
    FRONTEND_URL,
    BACKEND_URL,
]

CSRF_TRUSTED_ORIGINS = [FRONTEND_URL, BACKEND_URL]

# Django Rest Auth
REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "jwt-auth",
    "JWT_AUTH_REFRESH_COOKIE": "jwt-refresh",
    "JWT_AUTH_HTTPONLY": True,
    "JWT_AUTH_COOKIE_USE_CSRF": True,
}

# Django Allauth Settings
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": os.environ.get("GOOGLE_AUTH_CLIENT_ID", ""),
            "secret": os.environ.get("GOOGLE_AUTH_CLIENT_SECRET", ""),
            "key": "",
        },
        "SCOPE": [
            "profile",
            "email",
        ],
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"  # TODO: make it required for production
ACCOUNT_SIGNUP_REDIRECT_URL = f"{FRONTEND_URL}/discover"
LOGIN_REDIRECT_URL = f"{FRONTEND_URL}/discover"

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
