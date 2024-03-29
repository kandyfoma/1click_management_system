"""
Django settings for one_click_management_systeme project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_on_heroku
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k2z9po4i#n+1p(^ny1el2c!om(^-l+_%&ob0azk0-ike*-)81e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'mathfilters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # local
    'store.apps.StoreConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'one_click_management_systeme.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'one_click_management_systeme.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'one_click_management_systeme',
        'USER': 'one_click_management_systeme',
        'PASSWORD': 'adminadmin',
        'HOST': '127.0.0.1',
        'PORT': 5433,
        'CONN_MAX_AGE': 600,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
django_on_heroku.settings(locals())
AUTH_USER_MODEL = 'users.User'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
# ####################### JAZZMIN SETTINGS ##################################

JAZZMIN_SETTINGS = {
    "show_ui_builder": True,
    # title of the window (Will default to current_admin_site.site_title)
    "site_title": '1Click Management System Admin',
    # Title on the brand, and the login screen (19 chars max) (will default to current_admin_site.site_header)
    "site_header": '1Click Management System Admin',
    # Relative path to logo for your site, used for brand on top left (must be present in static files)
    "site_logo": "images/risa-logo.png",
    # CSS classes that are applied to the logo
    "site_logo_classes": "img-square",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "images/risa-logo.png",
    # Welcome text on the login screen
    "welcome_sign": "Welcome to 1Click Management System Admin,",
    # Copyright on the footer
    "copyright": "Copyright 1Click Management System",
    # Custom icons for side menu apps/models See the link below
    # https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,
    # 5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes

    "icons": {
        "users.user": "fas fa-user",
        "events.event": "fas fa-calendar-check",
        "events.import": "fas fa-file",
        "events.manager": "fas fa-user",
        "launch_event.managerproxy": "fas fa-user",
        "main_event.managerproxy": "fas fa-user",
        "risa_event.managerproxy": "fas fa-user",
        "events.guest": "fas fa-users",
        "launch_event.guestproxy": "fas fa-users",
        "main_event.guestproxy": "fas fa-users",
        "risa_event.guestproxy": "fas fa-users",
        "main_event.guesteventrelproxy": "fas fa-info",
        "events.ticket": "fas fa-gift",
        "main_event.goodiebagProxy": "fas fa-gift",
        "events.followup": "fas fa-list",
        "launch_event.registrationproxy": "fas fa-user-check",
        "risa_event.registrationproxy": "fas fa-user-check",
        "general.dropoffdate": "fas fa-calendar",
        "general.dropofftime": "fas fa-clock",
        "general.dropofflocation": "fas fa-building",
        "general.pickupdate": "fas fa-calendar",
        "general.pickuptime": "fas fa-clock",
        "general.pickuplocation": "fas fa-building",
        "general.hotel": "fas fa-bed",
        "general.category": "fas fa-music",
        "general.termsandcondition": "fas fa-handshake",
        "events.guesteventrel": "fas fa-home",
        "events.invoice": "fas fa-suitcase",
        "risa_event.guesteventrelproxy": "fas fa-bell",

    },

    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-angle-right",
    "order_with_respect_to": ["events", "events.event", "events.import", "events.manager", "events.guest",
                              "events.followup", "events.ticket", "events.guesteventrel", "events.invoice",
                              "events.partner", "launch_event", "launch_event.managerproxy", "launch_event.guestproxy",
                              "launch_event.registrationproxy", "main_event", "main_event.managerproxy",
                              "main_event.guestproxy", "main_event.guesteventrelproxy", "main_event.goodiebagProxy",
                              "risa_event", "risa_event.managerproxy", "risa_event.guestproxy",
                              "risa_event.guesteventrelproxy", "notifications", "notifications.managerproxy",
                              "notifications.guestproxy", "risa_event.registrationproxy",
                              "general", "users", "users.user"],
    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "Stock"}, {"app": "Commande"}, {"app": "Delivery"}, {"app": "User"},
        {"app": "Produit"},
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

    ],
    "usermenu_links": [
        {"name": "My Profile", "url": "/user/update/user/", "new_window": False},
        {"model": "users.user"}
    ],
}

JAZZMIN_UI_TWEAKS = {
    "theme": "minty",
    "dark_mode_theme": None,
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,

    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": False,

}