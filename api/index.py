from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):
 #handle a request for me 
 #methode to handle HTTP Get request 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return