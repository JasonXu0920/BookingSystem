# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.cinema import Cinema
from .api.cinema_search import CinemaSearch
from .api.cinema_offer import CinemaOffer
from .api.movie import Movie


routes = [
    dict(resource=Cinema, urls=['/cinema'], endpoint='cinema'),
    dict(resource=CinemaSearch, urls=['/cinema/search'], endpoint='cinema_search'),
    dict(resource=CinemaOffer, urls=['/cinema/offer'], endpoint='cinema_offer'),
    dict(resource=Movie, urls=['/movie'], endpoint='movie'),
]