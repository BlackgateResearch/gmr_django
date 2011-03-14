import os

DEBUG = True

path = os.path.dirname( __file__ )
TEMPLATE_DIRS = path + '/templates' 
MEDIA_ROOT = path + '/media'
MEDIA_URL = '/site_media/'

ADMINS = (
    ('Tristram Oaten', 'tris@blackgateresearch.com'),
    ('Karl Williams',  'karl@blackgateresearch.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'gmr.db'

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-uk'
USE_I18N = False

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

SITE_ID = 1

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$0+i)-09r+&hgt&zrx)y5q-#mr34*c(x2i9*+&#)1_+417ejxg'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',

    # django 1.2 only
    'django.contrib.messages.context_processors.messages',

    # required by django-admin-tools
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'gmr_django.urls'

gmr_template = os.path.dirname( __file__ ) + '/templates' 
TEMPLATE_DIRS = (gmr_template)

#unused?
#gmr_doc_root = os.path.dirname( __file__ ) + '/site_media'
#STATIC_DOC_ROOT = gmr_doc_root

ADMIN_TOOLS_THEMING_CSS = 'admin_tools/css/theming.css'

ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
#ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'gmr_django.dashboard.CustomAppIndexDashboard'

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'debug_toolbar',
    'django_extensions',
    'gmr_django.artist',
    'gmr_django.track',
)
