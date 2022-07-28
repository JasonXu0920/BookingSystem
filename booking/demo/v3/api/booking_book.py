# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from . import Resource
from .. import schemas
import sqlite3

class BookingBook(Resource):

    def post(self):
        cinema = g.args.get('cinema name')
        movie = g.args.get('movie name')
        username = g.args.get('username')
        number = int(g.args.get('number of tickets'))
        time = g.args.get('time slot')

        con = sqlite3.connect('booking.db')
        cur = con.cursor()

        cur.execute("INSERT INTO booking VALUES (cinema,username,movie,time,number)")

        con.commit()
        con.close()

        return make_response({'summary:':(cinema,username,movie,time,number)}, 201)