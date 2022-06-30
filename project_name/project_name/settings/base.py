from pathlib import Path

# Base conf
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ROOT_URLCONF = 'projet_name.urls'
WSGI_APPLICATION = 'projet_name.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static conf
STATIC_URL = 'static/'

# TimeZone conf
USE_TZ = True
TIME_ZONE = 'Europe/Moscow'

# Language conf
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'ru-ru'

INSTALLED_APPS = [
    # other apps
    # ...
    'corsheaders',
    'rest_framework',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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
