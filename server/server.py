from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Server(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        # self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.end_headers()

        print(self.requestline)

        message = 'Hello world'
        # self.wfile.write(bytes(message, "utf8"))
        self.wfile.write(json.dumps({'response': message}).encode('utf-8'))

with HTTPServer(('', 8000), Server) as server:
    server.serve_forever()