#!/usr/bin/env python

from tumblr import Api
from pygooglechart import PieChart3D

chart = PieChart3D(400, 200)
api = Api('staff.tumblr.com')
freq = {}
posts = api.read()
for post in posts:
	type = post['type']
	try:
		freq[type] += 1
	except:
		freq[type] = 1
chart.add_data(freq.values())
chart.set_pie_labels(freq.keys())
chart.set_title('staff.tumblr.com')
chart.download('staff.png')

