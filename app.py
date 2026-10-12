from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'hello')

    def log_message(self, format, *args):
        pass  # Suppress default logging


if __name__ == '__main__':
    server = HTTPServer(('localhost', 3000), HelloHandler)
    print('Server is running on http://localhost:3000')
    server.serve_forever()
