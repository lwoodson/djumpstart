# Development environment appropriate settings.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'asda9234jks8934'

DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'djumpstart',
      'USER': 'postgres',
      'PASSWORD': '',
      'HOST': '',
      'PORT': '',
    }
}

# DebugToolbar config
ENV_MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
ENV_INSTALLED_APPS = (
    'debug_toolbar',
)
INTERNAL_IPS = ('127.0.0.1',)
