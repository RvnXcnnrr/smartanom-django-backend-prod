"""
Django settings for SmarTanom project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-x9!4w46i-%68mn9hcr2w73rf$nz26kfug3=3x35!*#$abc#pj8')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Allow all hosts in development, specific hosts in production
ALLOWED_HOSTS = ['*']  # Allow all hosts for easier development and emulator access

# Database configuration
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Add whitenoise middleware for static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS settings - allow all origins for easier development and emulator access
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Keep the specific origins for reference, but with CORS_ALLOW_ALL_ORIGINS=True, these won't be used for restriction
CORS_ALLOWED_ORIGINS = [
    "https://smartanom-frontend.onrender.com",
    "http://localhost:8081",
    "http://127.0.0.1:8081",
    "http://10.0.2.2:8081",  # Android emulator special IP for localhost
    "http://10.0.2.16:8081", # Your Android emulator IP
    "http://10.0.2.2:19006",  # Android emulator for Expo
    "http://10.0.2.16:19006", # Your Android emulator IP for Expo
    "http://localhost:19006",
    "http://127.0.0.1:19006",
    "https://smartanom-django-backend-prod.onrender.com",
    "https://smartanom-backend.onrender.com",
    "exp://10.0.2.2:8081",    # Expo on Android emulator
    "exp://10.0.2.16:8081",   # Expo on your Android emulator
    "exp://localhost:8081",   # Expo on web
    "exp://127.0.0.1:8081",   # Expo alternative
    # The following line allows any subdomain
    "https://*.expo.dev",     # For Expo Go on physical devices
    "exp://*",                # Any Expo URL
]

# Security settings for production
if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# Application definition

INSTALLED_APPS = [
    'accounts.apps.AccountsConfig',  # This must come before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'hydroponics',
    'corsheaders',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
APPEND_SLASH = False

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # This must come first
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# CORS settings (ensure these are correct)
CORS_ALLOW_CREDENTIALS = True
# Only enable this for development
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8081",
    "http://127.0.0.1:8081",
    "http://10.0.2.2:8081",
    "http://localhost:19006",  # For React Native development
    "http://127.0.0.1:19006",  # For React Native development
    # Add your frontend's production URL if needed
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# For React Native, allow all headers
CORS_ALLOW_ALL_HEADERS = True

# Allow all methods
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

# Expose necessary headers
CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken', 'Authorization']

# Add CSRF trusted origins to match CORS allowed origins
CSRF_TRUSTED_ORIGINS = [
    "https://smartanom-frontend.onrender.com",
    "http://localhost:8081",
    "http://127.0.0.1:8081",
    "https://smartanom-django-backend-prod.onrender.com",
    "https://smartanom-backend.onrender.com",
    "https://*.expo.dev",
]

ROOT_URLCONF = 'SmarTanom.urls'

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

WSGI_APPLICATION = 'SmarTanom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES['default'] = dj_database_url.parse("postgresql://smartanom_database_user:SatlaaFv06NK6e5WDkicijieqndGoVzJ@dpg-d0i7hpl6ubrc73d8fnag-a.singapore-postgres.render.com/smartanom_database")

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'accounts.User'

FRONTEND_URL = 'http://localhost:8081'  

#  Updated: Gmail SMTP email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'reyfoxconner@gmail.com'  #  Replace with your Gmail address
EMAIL_HOST_PASSWORD = 'wvuy cxnj bczr rhuq'  #  Use your Gmail App Password

DEFAULT_FROM_EMAIL = 'noreply@smartanom.com'

AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailBackend',  # Custom backend for email login
    'django.contrib.auth.backends.ModelBackend',  # Fallback
]

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
