# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from . import Resource
from .. import schemas
from .wit import call_wit
from rivescript import RiveScript
import requests
import os
import json

name = ''
email = ''
class Ask(Resource):

    def get(self):
        rs = RiveScript()
        rs.load_directory(os.path.join(os.path.dirname(__file__), '.', 'brain'))
        rs.sort_replies()

        msg = g.args.get('message')
        reply = rs.reply('localuser', msg)

        if 'ERR' in reply:
            reply = call_wit(msg)

        print('movie bot: ', reply)
        return make_response({'reply': reply}, 200)