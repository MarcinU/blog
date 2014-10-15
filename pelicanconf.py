#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hrv'
SITENAME = 'Harv\'s -log'
SITEURL = 'http://harv.pl'

THEME = '/home/harv/blog/pelican-bootstrap3'
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
	 ('Seventstring', 'http://seventring.pl/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/harvpl'),
          ('github', 'http://github.com/marcinu'),)

DEFAULT_PAGINATION = 6

ARTICLE_URL = '/blog/{slug}.html'
#ARTICLE_URL = '/{date:%Y}/{date:%m}/{date:%d}/{slug}/'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GITHUB_URL = 'http://github.com/MarcinU/'

TYPOGRIFY = True
