#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'kwdfm'
SITENAME = u"kwdfm's blog"
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'
DATE_FORMATS = {'zh':'%Y-%m-%d %H:%M'}

GITHUB_URL = 'https://github.com/kwdfmzhu'

#THEME = 'bootstrap2'
#THEME = 'cebong'
#THEME = 'pelican-bootstrap3'
#THEME = 'pelican-hss' #OK
THEME = 'pelican-fresh'

#ITELOGO = 'images/logo.png'
#FAVICON = 'images/logo.png'


FEED_ALL_RSS =  'feeds/all.rss.xml'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
            ('Github', 'https://github.com/kwdfmzhu'),
        )

# Social widget
SOCIAL = (
            ('Github', 'https://github.com/kwdfmzhu'),
            (u'知乎', 'https://www.zhihu.com/people/kwdfmzhu'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


#PLUGIN_PATH = u"pelican-plugins"
#PLUGINS = ["sitemap"]
#SITEMAP = {
#    "format": "xml",
#    "priorities": {
#        "articles": 0.7,
#        "indexes": 0.5,
#        "pages": 0.3,
#    },
#    "changefreqs": {
#        "articles": "monthly",
#        "indexes": "daily",
#        "pages": "monthly",
#    }
#}
