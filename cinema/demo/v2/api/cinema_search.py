# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from . import Resource
from .. import schemas
import sqlite3



class CinemaSearch(Resource):

    def get(self):
        name = (g.args.get('movie name')).lower()
        con = sqlite3.connect('cinema.db')
        cur = con.cursor()

        cinemas = {}
        for row in cur.execute('SELECT * FROM cinema ORDER BY seats'):
            if name in row:
                cinemas.add(row[1])

        con.close()
        return make_response({'these are the cinemas with the movie':cinemas}, 200)