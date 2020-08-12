ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', 'jobs.harenconstruction.com', 'www.harenconstruction.com', 'harenconstruction.com' '104.236.59.248']

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = '/home/applicant/' #os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# 'ENGINE': 'django.db.backends.sqlite3',
# 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'applicant',
        'USER': 'applicant',
        'PASSWORD': 's34vZuhX&ChX@Lre0%kL',
        'HOST': 'localhost',
        'PORT': '',
    }
}


TEMPLATE_PATH = os.path.join('/home/applicant/applicant/applicant/', 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

# Media (user uploaded files)
MEDIA_ROOT = os.path.join('/home/applicant/', 'media')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_PATH = os.path.join('/home/applicant/', 'static')
STATIC_ROOT = STATIC_PATH
STATICFILES_DIRS = [
    os.path.join('/home/applicant/applicant/applicant/', "static"),
]
STATIC_URL = '/static/'

# Fixtures for developer data.
FIXTURE_DIRS = [
    os.path.join('/home/applicant/applicant/applicant/', "fixtures"),
]

# temporary path for wizard assisted file uploads
TEMP_PATH = os.path.join('/home/applicant/', 'tmp')

# logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/home/applicant/applicant.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
