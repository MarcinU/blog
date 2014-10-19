#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hrv'
SITENAME = '$ cat /dev/Hrv'
SITEURL = 'http://harv.pl'

PATH = 'content'
STATIC_PATHS = ['images','uploads','extra/my.css']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
	 ('Sevenstring', 'http://sevenstring.pl/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/harvpl'),
          ('github', 'http://github.com/marcinu'),)

DEFAULT_PAGINATION = 6

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS= 'blog/{slug}.html'
CATEGORY_URL = "{slug}"
CATEGORY_SAVE_AS = "{slug}/index.html"


#PLUGINS
PLUGIN_PATHS = ["/home/harv/blog/plugins/pelican-plugins"]
PLUGINS = ["html_rst_directive", "pelican_gist", "summary"]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#THEME 
THEME = '/home/harv/blog/themes/pelican-bootstrap3'
GITHUB_URL = 'http://github.com/MarcinU/'

TYPOGRIFY = True
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS =50 
DISPLAY_TAGS_INLINE = True

BOOTSTRAP_NAVBAR_INVERSE = True
DISPLAY_BREADCRUMBS = True
PYGMENTS_STYLE = 'vim'

EXTRA_PATH_METADATA = {
    'extra/my.css': {'path': 'static/my.css'}
}
CUSTOM_CSS = 'static/my.css'

#SITELOGO = 'images/my_site_logo.png'


