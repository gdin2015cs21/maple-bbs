# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_sockets import Sockets

site1 = Blueprint('ws', __name__)


def init_app(app):
    from .views import WsChat

    ws_chat = WsChat.as_view('ws_chat')     # websocket
    site1.add_url_rule('/ws', view_func=ws_chat)

    sockets = Sockets(app)
    sockets.register_blueprint(site1)


