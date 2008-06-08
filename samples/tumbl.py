#!/usr/bin/env python

from tumblr import Api
import sys

BLOG='YOU.tumblr.com'
USER='YOUREMAIL'
PASSWORD='YOURPASSWORD'

if len(sys.argv) != 3:
	print "Usage: tumbl <title> <body>"
	sys.exit(-1)	

title = sys.argv[1]
body = sys.argv[2]

api = Api(BLOG,USER,PASSWORD)
post = api.write_regular(title,body)
print "Published: ", post['url']
