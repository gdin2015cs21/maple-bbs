# -*- coding: utf-8 -*-
from flask import render_template, jsonify, request, session
import json
from forums.common.views import IsAuthMethodView, MethodView
user_dict = {}


class WsChat(MethodView):
    def get(self, user_socket):
        print('session', session)
        username = session['user_id']
        user_dict[username] = user_socket
        while not user_socket.closed:
            msg = user_socket.receive()  # 等待接收客户端发来的数据
            if msg is None:
                # user_socket.close()
                user_dict.pop(username)
                break
            msg_dict = json.loads(msg)
            msg_dict['from_user'] = username
            to_user = msg_dict.get('to_user')
            user_length = len(user_dict)
            msg_dict['user_length'] = user_length
            if to_user is None:  # 如果用户名是空表示群发
                for uname, uwebsocket in user_dict.items():
                    if uname == username:  # 群发时不用给自己发
                        continue
                    uwebsocket.send(json.dumps(msg_dict))
                continue
        return jsonify('关闭成功')

