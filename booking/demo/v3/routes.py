# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.booking_book import BookingBook
from .api.booking_cancel import BookingCancel


routes = [
    dict(resource=BookingBook, urls=['/booking/book'], endpoint='booking_book'),
    dict(resource=BookingCancel, urls=['/booking/cancel'], endpoint='booking_cancel'),
]