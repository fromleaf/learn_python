# -*- coding: utf-8 -*-

import httplib
import os
from urlparse import urljoin, urlunparse
from urllib import urlretrieve
from HTMLParser import HTMLParser

class ImageParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		if tag != 'img':
			return
		if not hasattr(self, 'result'):
			self.result = []

		for name, value in attrs:
			if name == 'src':
				self.result.append(value)


def downloadImage(srcUrl, data):
	if not os.path.exists('DOWNLOAD'):
		os.makedirs('DOWNLOAD')
	
	parser = ImageParser()
	parser.feed(data)
	result_set = set(x for x in parser.result)

	for x in sorted(result_set):
		src = urljoin(srcUrl, x)
		base_name = os.path.basename(src)
		target_file = os.path.join('DOWNLOAD', base_name)

		print "Downloading...", src
		urlretrieve(src, target_file)


def main():
	host = "www.google.com"

	conn = httplib.HTTPConnection(host)
	conn.request("GET", '')
	resp = conn.getresponse()

	charset = resp.msg.getparam('charset')
	data = resp.read().decode(charset)
	conn.close()

	print "\n>>>>>>>> Download Images from ", host
	url = urlunparse(('http', host, '', '', '', ''))
	downloadImage(url, data)


if __name__ == '__main__':
	main()
