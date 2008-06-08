#!/usr/bin/env python

from tumblr import Api
import feedparser

BLOG='YOU.tumblr.com'
USER='YOUREMAIL'
PASSWORD='YOURPASSWORD'

api = Api(BLOG,USER,PASSWORD)
d = feedparser.parse('http://feeds.weatherbug.com/rss.aspx?zipcode=27702&feed=curr&zcode=z4641')
for e in d.entries:
    api.write_regular(e.title,e.summary)

