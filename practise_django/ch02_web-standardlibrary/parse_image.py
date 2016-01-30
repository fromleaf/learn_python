# -*- coding: utf-8 -*-

from urllib2 import urlopen
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


def parseImage(data):
	parser = ImageParser()
	parser.feed(data)
	data_set = set(x for x in parser.result)
	print '\n'.join(sorted(data_set))

def main():
	url = "http://www.google.com"

	f = urlopen(url)
	charset = f.info().getparam('charset')
	data = f.read().decode(charset)
	f.close()

	print "\n>>>>>>>> Fetch Images from", url
	parseImage(data)

if __name__ == '__main__':
	main()
