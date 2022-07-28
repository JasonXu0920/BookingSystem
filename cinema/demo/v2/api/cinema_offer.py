# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from . import Resource
from .. import schemas


class CinemaOffer(Resource):

    def get(self):
        name = (g.args.get('cinema name')).lower()
        offers = {'event cinema': 'popcorn+softdrinks : 12 dollars, popcorn+snacks : 10 dollars',
                  'hoyts cinema': 'popcorn+drinks : 15 dollars, popcorn+snacks : 9 dollars',
                  'palace cinema': 'popcorn+snacks : 10 dollars, popcorn+softdrinks : 13 dollars'}

        return make_response({'The offers are': offers[name]}, 200)