# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_sockets import Sockets

site1 = Blueprint('ws', __name__)
site2 = Blueprint('chat', __name__)


def init_app(app):
    from .views import WsChat, Webchat

    ws_chat = WsChat.as_view('ws_chat')     # websocket
    webchat = Webchat.as_view('webchat')    # 聊天界面

    site1.add_url_rule('/ws', view_func=ws_chat)
    site2.add_url_rule('/chat/webchat', view_func=webchat)

    sockets = Sockets(app)
    sockets.register_blueprint(site1)

    app.register_blueprint(site2)
