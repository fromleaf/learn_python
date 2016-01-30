#!/usr/bin/env python
#

import urllib2
from urllib import urlencode

url = "http://localhost:8888/cgi-bin/script.py"
data = {
	'language': 'python',
	'framework': 'django',
	'email': 'heo@test.com'
}
enc_data = urlencode(data)

f = urllib2.urlopen(url, enc_data)			# POST
print f.read()
