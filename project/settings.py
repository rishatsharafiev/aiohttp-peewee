import asyncio
import uvloop
import pathlib
from envparse import env

# from project.utils.logger_filters import RequestIdLogFilter
from project.utils.peewee import get_pool, get_manager

env.read_envfile()

# Base path
BASE_PATH = pathlib.Path(__file__).parent

# Debug
DEBUG = env('DEBUG', cast=bool, default=False)

# Application
APP_HOST = env('APP_HOST', cast=str, default='localhost')
APP_PORT = env('APP_PORT', cast=int, default=8080)

# Templates
TEMPLATES_PATH = BASE_PATH / 'templates'

# Static
STATIC_PATH = BASE_PATH / 'static'
STATIC_URL = '/static'

# Database
PG_NAME = env('PG_NAME', cast=str, default='')
PG_USER = env('PG_USER', cast=str, default='')
PG_PASSWORD = env('PG_PASSWORD', cast=str, default='')
PG_HOST = env('PG_HOST', cast=str, default='localhost')
PG_PORT = env('PG_PORT', cast=int, default=5432)
PG_MAX_CONNECTIONS = env('PG_MAX_CONNECTIONS', cast=int, default=2)

# Cookie
COOKIE_SECRET = env('COOKIE_SECRET', cast=str, default='')

# Logging
SENTRY_DSN = env('SENTRY_DSN', cast=str, default='')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(process)d %(name)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'peewee.async': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'peewee': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'bot': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'aiohttp.access': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

# Init loop and manager
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

loop = asyncio.get_event_loop()
pool = get_pool(PG_NAME, PG_USER, PG_PASSWORD, PG_HOST, PG_PORT, PG_MAX_CONNECTIONS)
manager = get_manager(pool, loop)
