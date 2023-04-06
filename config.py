#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016-2019 jianglin
# File Name: config.example
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2016-05-20 12:31:46 (CST)
# Last Update: Monday 2022-12-12 16:40:46 (CST)
#          By: jianglin
# Description:
# **************************************************************************
from datetime import timedelta
from os import path
from urllib.parse import quote

PATH = path.abspath(path.dirname(__file__))
DEBUG = True
SECRET_KEY = 'xxxxx'
SECURITY_PASSWORD_SALT = 'xxxxx'
SECRET_KEY_SALT = 'xxxxx'

# avatar upload directory
AVATAR_FOLDER = path.join(PATH, 'avatars')
# avatar generate range
AVATAR_RANGE = [122, 512]

# for development use localhost:5000
# for production use xxx.com
# SERVER_NAME = 'localhost:5000'

# remember me to save cookies
PERMANENT_SESSION_LIFETIME = timedelta(days=3)
REMEMBER_COOKIE_DURATION = timedelta(days=3)
ONLINE_LAST_MINUTES = 5

# You want show how many topics per page
PER_PAGE = 12

# Use cache
CACHE_TYPE = 'redis'
CACHE_DEFAULT_TIMEOUT = 60
CACHE_KEY_PREFIX = 'cache:'
CACHE_REDIS_HOST = '192.168.0.101'
CACHE_REDIS_PORT = '6379'
CACHE_REDIS_PASSWORD = 'xxxxxx'
CACHE_REDIS_DB = 2

# Redis setting
REDIS = {
    'host': '192.168.0.101',
    'db': 1,
    'password': 'xxxxx',
    'decode_responses': True
}

# some middleware
MIDDLEWARE = [
    'forums.common.middleware.GlobalMiddleware',
    'forums.common.middleware.OnlineMiddleware'
]

# Mail such as qq
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "xxxxx@qq.com"
MAIL_PASSWORD = "xxxxxx"
MAIL_DEFAULT_SENDER = 'xxxxx@qq.com'
# MAIL_SUPPRESS_SEND = True

# SERVER_NAME = 'localhost:8000'
SUBDOMAIN = {'forums': False, 'docs': False}

# logging setting
LOGGING = {
    'info': 'logs/info.log',
    'error': 'logs/error.log',
    'send_mail': False,
    'toaddrs': [],
    'subject': 'Your Application Failed',
    'formatter': '''
            Message type:       %(levelname)s
            Location:           %(pathname)s:%(lineno)d
            Module:             %(module)s
            Function:           %(funcName)s
            Time:               %(asctime)s

            Message:

            %(message)s
            '''
}

# Sql
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:{}@192.168.0.101/postgres'.format(quote('xxxxxx'))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

MSEARCH_INDEX_NAME = 'msearch'
MSEARCH_BACKEND = 'whoosh'
# SQLALCHEMY_ECHO = True
# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
# SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'
BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = 'UTC'
BABEL_TRANSLATION_DIRECTORIES = path.join(PATH, 'translations')
