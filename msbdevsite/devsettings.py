from msbdevsite.settings import *

DEBUG = True

ALLOWED_HOSTS = [
    u'www.msb.dev',
    '127.0.0.1',
    'localhost',
]

SECRET_KEY = "asbfibasifbaskutdkdbvksakjb"

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
