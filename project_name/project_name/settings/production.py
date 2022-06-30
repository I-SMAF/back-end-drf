import os
from .base import *

DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = [os.getenv('ALLOWED_HOST', '*')]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    # other db like:
    # 'abitur_list': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'abitur_list',
    #     'USER': os.getenv('DB_USER'),
    #     'PASSWORD': os.getenv('DB_PASSWORD'),
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # },
}
STATICFILES_DIRS = [
    BASE_DIR / 'front_end' / 'build' / 'static',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # if work with React:
        # 'DIRS': [
        #     BASE_DIR / 'front_end',
        # ],
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
