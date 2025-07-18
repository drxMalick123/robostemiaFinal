"""
Django settings for startup project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=jxwyxxtjai7v6cu)1w2l!9^xx(&#6ph%%9q=z1!$#!o9ncc71'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [
    "https://www.robostemia.com"
]

ALLOWED_HOSTS = [
    "robostemia.com",
    "www.robostemia.com",
    "robostemia.onrender.com",  # Optional, for Render default domain
    "localhost",                # Optional, for local dev
    "127.0.0.1"
]

# Application definition

INSTALLED_APPS = [
    'jazzmin',
 'robot.apps.RobotConfig', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'channels',
    'adminsortable2',
    
]

# ASGI_APPLICATION = 'yourprojectname.asgi.application'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'startup.urls'

TEMPLATES = [
    {
         'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'startup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'


# Set this to India time
TIME_ZONE = 'Asia/Kolkata'

# Make Django use timezone-aware datetime
USE_TZ = True
USE_I18N = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / "static"]  # Optional for project-level static
STATIC_ROOT = BASE_DIR / "staticfiles"

# STATICFILES_DIRS = [
#     BASE_DIR / "static",  # ✅ makes sure your static/fonts is served
# ]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




JAZZMIN_SETTINGS = {
    # Branding
    "site_title": "Robostemia Admin",
    "site_header": "Robostemia Control Panel",
    "site_brand": "Robostemia",
    "welcome_sign": "Welcome to Robostemia Admin 👋",
    "copyright": "© 2025 Robostemia",

    # Logos (stored inside static/robot/)
    "site_logo": "robot/logo1.png",         # Appears in the navbar
    "login_logo": "robot/logo.png",         # Appears on login page

    # Layout Controls
    "show_sidebar": True,
    "navigation_expanded": True,
    "related_modal_active": True,
    "order_with_respect_to": ["auth", "robot"],
    "hide_apps": [],

    # Top Navigation
    "topmenu_links": [
        {"name": "🏠 Home", "url": "/", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"app": "robot"},
    ],

    # FontAwesome Icons for models/apps
"icons": {
    "auth": "fas fa-users-cog",
    "auth.user": "fas fa-user",
    "auth.Group": "fas fa-users",

    # robot app models
    "robot.Person": "fas fa-robot",
    "robot.Product": "fas fa-box",
    "robot.Services": "fas fa-cogs",
    "robot.Order": "fas fa-shopping-cart",
    "robot.ContactMessage": "fas fa-envelope",
    "robot.HomePageImgSlider": "fas fa-images",
    "robot.AdvisoryCommitteeMember": "fas fa-user-tie",
    "robot.Costomer_Oder_list_details": "fas fa-clipboard-list",
    "robot.UserCartItem": "fas fa-cart-plus",
    "robot.OrderItem": "fas fa-box-open",
},

    # Custom CSS (optional for styling forms, layout tweaks)
    "custom_css": "css/my-jazzmin5.css",

    # Quick links inside admin
    "custom_links": {
        "auth": [{
            "name": " Change Password",
            "url": "admin:password_change",
            "icon": "fas fa-key",
            "permissions": ["auth.change_user"]
        }]
    },

    # UI Style Tweaks
    "ui_tweaks": {
        "navbar_small_text": False,
        "footer_small_text": True,
        "body_small_text": False,
        "brand_small_text": False,
        "accent": "accent-info",              # Color scheme (info/primary/success)
        "navbar": "navbar-dark",              # navbar-light / navbar-dark
        "sidebar": "sidebar-light-info",      # sidebar-dark-primary / sidebar-light-info
        "theme": "flatly",                    # flatly, cerulean, cyborg, etc.
        "dark_mode_theme": "darkly",          # optional dark mode
        "login_bg": None,                     # custom image if needed
        "no_navbar_border": False
    }
}
JAZZMIN_UI_TWEAKS = {

#    "theme": "sketchy",
}
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'  # After logout
