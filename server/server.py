from http.server import HTTPServer, BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        message = 'Hello world'
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8000), Server) as server:
    server.serve_forever()