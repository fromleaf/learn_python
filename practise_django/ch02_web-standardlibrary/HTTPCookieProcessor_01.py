# -*- coding: utf-8 -*-

import urllib2

# 쿠키 핸들러 생성, 쿠키 데이터 처리를 디폹로 CookieJar 를객체를 사용함
cookie_handler = urllib2.HTTPCookieProcessor()

opener = urllib2.build_opener(cookie_handler)
urllib2.install_opener(opener)
# 쿠키 데이터와 함께 서버로 요청
u = urllib2.urlopen('http://www.example.com/login.html')
