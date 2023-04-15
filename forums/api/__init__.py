#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-20 15:49:33 (CST)
# Last Update: Wednesday 2019-05-08 15:43:20 (CST)
#          By:
# Description:
# **************************************************************************
from werkzeug import import_string


def init_app(app):
    blueprints = [
        "forums.api.forums",
        "forums.api.topic",
        "forums.api.tag",
        "forums.api.user",
        "forums.api.collect",
        "forums.api.message",
        "forums.api.follow",
        "forums.api.upload",
        "forums.api.setting",
        "forums.api.search",
        "forums.api.chat",
    ]
    for blueprint in blueprints:
        import_string(blueprint).init_app(app)
