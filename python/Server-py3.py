#sample code to run a server using python 3 
#https://docs.python.org/3/library/http.server.html


from http.server import CGIHTTPRequestHandler, HTTPServer

handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin', '/htbin']  # this is the default
server = HTTPServer(('localhost', 8123), handler)
server.serve_forever()

