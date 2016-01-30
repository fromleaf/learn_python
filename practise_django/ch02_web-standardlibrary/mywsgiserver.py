def my_app(environ, start_response):

	status = "200 OK"
	headers = [ ('Content-Type', 'text/plain') ]
	start_response(status, headers)

	return ["This is a sample WSGI App."]

if __name__ == '__main__':
	from wsgiref.simple_server import make_server

	print "Start WSGI Server on port 8888..."
	server  = make_server('', 8888, my_app)
	server.serve_forever()
