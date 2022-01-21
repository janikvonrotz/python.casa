import http.server
import socketserver

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'mypage.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
handler = HttpRequestHandler

server = socketserver.TCPServer(("", 8000), handler)

# Start the server
server.serve_forever()
