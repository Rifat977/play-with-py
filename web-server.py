from http.server import BaseHTTPRequestHandler, HTTPServer
import time

HOST = "localhost"
PORT = 8000

class RifatHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Hello World!</h1></body></html>", "utf-8"))


server = HTTPServer((HOST, PORT), RifatHTTP)
print("Server running..")

server.serve_forever()
server.serve_close()
print("Server stopped")
