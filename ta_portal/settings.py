"""
Django settings for ta_portal project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ay0lu)jff!uh=a1389s9m2ps#q)+019g*-f&##9jdh&zkv*wv8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student_faculty.apps.StudentFacultyConfig',
    'login.apps.LoginConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ta_portal.urls'

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

WSGI_APPLICATION = 'ta_portal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

#SECRET_KEY = 'lu3+xlyjj940k46e!h$wp#_l5^g4eb4zr(*a286=o6!@di8cbg'

BASE_URL = 'https://gymkhana.iitb.ac.in/~ugacademics/TA_PORTAL/'
STATIC_BASE_URL = 'https://gymkhana.iitb.ac.in/~ugacademics/TA_PORTAL/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['temp-iitb.radialapps.com']

SSO_TOKEN_URL = 'https://gymkhana.iitb.ac.in/sso/oauth/token/'
SSO_STUDENT_PROFILE_URL = 'https://gymkhana.iitb.ac.in/sso/user/api/user/?fields=first_name,last_name,type,sex,username,email,program,contacts,insti_address,secondary_emails,mobile,roll_number'
SSO_FACULTY_PROFILE_URL = 'https://gymkhana.iitb.ac.in/sso/user/api/user/?fields=first_name,last_name,type,sex,username,email,program'
SSO_CLIENT_ID = 'z3E7yusTYcwJVy1o3AsFVro2EC18ntwAnBEIJLM4'
SSO_CLIENT_ID_SECRET_BASE64 = 'ejNFN3l1c1RZY3dKVnkxbzNBc0ZWcm8yRUMxOG50d0FuQkVJSkxNNDpRbHpjUlliVkxtMWhNRlBYNm5jd3Y0Qzc1b1V4UlRydXZ3NG1zb1hVa0c1eTdpQzhncjJyMm5rbndyZUQzRmlFM1l4V2diMXdYMjJFU3VPWDk4ZVY4RExobEtzbzZBMlhsNkhEWHpNVEtFRTZqOFlVNEN0ZGV6SmJOUmxscVI4RA=='

# Flip for broken external server certificates
SSO_BAD_CERT = False
