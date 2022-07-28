# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from . import Resource
from .. import schemas
import sqlite3

class Movie(Resource):

    def get(self):
        cinema = g.args.get('cinema name')
        movie = g.args.get('movie name')
        con = sqlite3.connect('cinema.db')
        cur = con.cursor()

        timeslots = []
        for row in cur.execute('SELECT * FROM cinema ORDER BY seats'):
            if cinema in row and movie in row:
                timeslots.append(row)
        con.close()

        return make_response({'we got these time slots':timeslots}, 200)