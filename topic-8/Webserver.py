import http.server
import socketserver

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'mypage.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Erstelle ein Objekt anhand der obigen Klasse
handler = HttpRequestHandler

server = socketserver.TCPServer(('', 1234), handler)

# Starte den Server
server.serve_forever()
