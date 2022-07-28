# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from . import Resource
from .. import schemas


class Cinema(Resource):

    def get(self):
        cinemas = ['event cinema', 'hoyts cinema', 'palace cinema']
        return make_response({"these are the cinemas":cinemas}, 200)