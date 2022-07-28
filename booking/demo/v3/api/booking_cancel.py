# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from . import Resource
from .. import schemas
import sqlite3

class BookingCancel(Resource):

    def delete(self):
        cinema = g.args.get('cinema name')
        movie = g.args.get('movie name')
        username = g.args.get('username')
        time = g.args.get('time slot')

        con = sqlite3.connect('booking.db')
        cur = con.cursor()


        cur.execute("""DELETE from booking where username is ?""", (username))

        con.commit()
        con.close()

        return make_response({'cancel the booking': (cinema,username,movie,time)}, 200)