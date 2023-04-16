# -*- coding: utf-8 -*-
from flask import Blueprint

site2 = Blueprint('chat', __name__)


def init_app(app):
    from .views import Webchat
    webchat = Webchat.as_view('webchat')    # 聊天界面

    site2.add_url_rule('/chat/webchat', view_func=webchat)
    app.register_blueprint(site2)
