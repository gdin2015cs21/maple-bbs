#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-17 20:45:08 (CST)
# Last Update: Wednesday 2019-05-08 14:37:48 (CST)
#          By:
# Description:
# **************************************************************************
from flask import render_template, request

from forums.api.topic.db import Topic
from forums.common.views import BaseMethodView as MethodView
from forums.common.utils import (gen_filter_dict, gen_order_by)
from flask_babel import gettext as _
from forums.api.utils import gen_topic_filter, gen_topic_orderby

from .db import Board


class IndexView(MethodView):
    def get(self):
        # topics = Topic.query.filter_by(
        #     is_good=True, is_top=False).paginate(1, 10)
        top_topics = Topic.query.filter_by(is_top=True).limit(5)

        keys = ['title']
        request_data = request.data
        orderby = gen_topic_orderby(request_data, keys)
        params = gen_topic_filter(request_data, keys)

        if request.path.endswith('good'):
            params.update(is_good=True)
        elif request.path.endswith('top'):
            params.update(is_top=True)

        topics = Topic.query.filter_by(**params).order_by(*orderby).paginate(1, 10)

        if not topics.items:
            topics = Topic.query.filter_by(is_top=False).paginate(1, 10)
        data = {'topics': topics, 'top_topics': top_topics}
        return render_template('forums/index.html', **data)


class AboutView(MethodView):
    def get(self):
        return self.render_template('forums/about.html')


class HelpView(MethodView):
    def get(self):
        return self.render_template('forums/help.html')


class ContactView(MethodView):
    def get(self):
        return self.render_template('forums/contact.html')


class BoardListView(MethodView):
    def get(self):
        boards = Board.query.filter_by(parent_id=None).order_by("-name").all()
        data = {'boards': boards}
        return render_template('board/board_list.html', **data)


class BoardView(MethodView):
    def get(self, pk):
        board = Board.query.filter_by(id=pk).first_or_404()
        has_children = board.child_boards.exists()
        topics = self.topics(pk, has_children)
        data = {'board': board, 'topics': topics}
        return render_template('board/board.html', **data)

    def topics(self, pk, has_children):
        request_data = request.data
        page, number = self.pageinfo
        keys = ['title']
        # order_by = gen_order_by(request_data, keys)
        # filter_dict = gen_filter_dict(request_data, keys)
        order_by = gen_topic_orderby(request_data, keys)
        filter_dict = gen_topic_filter(request_data, keys)
        if has_children:
            o = []
            for i in order_by:
                if i.startswith('-'):
                    o.append(getattr(Topic, i.split('-')[1]).desc())
                else:
                    o.append(getattr(Topic, i))
            topics = Topic.query.filter_by(**filter_dict).outerjoin(Board).or_(
                Board.parent_id == pk, Board.id == pk).order_by(*o).paginate(
                    page, number, True)
            return topics
        filter_dict.update(board_id=pk)
        topics = Topic.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number, True)
        return topics
