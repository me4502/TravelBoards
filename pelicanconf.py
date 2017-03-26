#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'TravelBoards'
SITENAME = 'TravelBoards'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Brisbane'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

DIRECT_TEMPLATES = ['index', 'people', 'map', 'budget', 'timeline',
                    'itinerary', 'xp-choose', 'cloud']

CLOUD_PHOTOS = [
    'cloud_1.jpg', 'cloud_2.jpg', 'cloud_3.jpg', 'cloud_4.jpg', 'cloud_5.jpg',
    'cloud_7.jpg', 'cloud_8.jpg', 'cloud_9.jpg', 'cloud_10.jpg',
    'cloud_11.jpg'
]

THEME = "theme"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
