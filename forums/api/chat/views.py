# -*- coding: utf-8 -*-
from flask import render_template, session
from forums.api.user.db import User, UserInfo
from forums.common.views import IsAuthMethodView


class Webchat(IsAuthMethodView):
    def get(self):
        user_id = session['user_id']
        user = User.get(id=user_id)
        user_info = UserInfo.get(user_id=user_id)
        avatar = '/avatars/' + user_info.avatar if user_info.avatar else 'https://lmzh.top/avatars/%E8%84%91%E6%B4%9E%E5%90%9B%E5%97%B7-16808010077498.png'
        data = {'avatar': avatar, 'username': user.username, 'name': user.username}
        return render_template('chat/index.html', **data)
