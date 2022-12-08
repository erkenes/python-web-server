import os

from http.server import BaseHTTPRequestHandler

from routes.main import routes
from handlers.main import handlers
from urllib.parse import urlparse
from urllib.parse import parse_qs

from response.badRequestHandler import BadRequestHandler

class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_GET(self):
        parsed_url = urlparse(self.path)
        url_path = parsed_url.path

        split_path = os.path.splitext(url_path)
        request_extension = (split_path[1]).lstrip('.')

        if request_extension == 'py':
            handler = BadRequestHandler()
        elif request_extension == '' or request_extension in handlers:
            request_handler = request_extension
            request_path = url_path

            if url_path in routes:
                request_handler = routes[url_path]['handler']
                request_path = routes[url_path]

            if request_handler in handlers:
                query_params = parse_qs(parsed_url.query)

                handler = handlers[request_handler]
                handler.find(request_path, query_params)
            else:
                handler = BadRequestHandler()
        else:
            handler = BadRequestHandler()

        self.respond({
            'handler': handler
        })

    def handle_http(self, handler):
        status_code = handler.getStatus()

        self.send_response(status_code)

        if status_code == 200:
            content = handler.getContents()
            self.send_header('Content-type', handler.getContentType())
        else:
            content = '404 Not Found'

        self.end_headers()

        if isinstance(content, bytes):
            return content
        else:
            return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['handler'])
        self.wfile.write(response)