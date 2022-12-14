import os

from response.requestHandler import RequestHandler


class StaticHandler(RequestHandler):
    def __init__(self):
        self.filetypes = {
            'js': 'text/javascript',
            'css': 'text/css',
            'jpg': 'image/jpeg',
            'png': 'image/png',
            'ico': 'image/x-icon',
            'undefined': 'text/plain'
        }

    def find(self, file_path, query_params):
        split_path = os.path.splitext(file_path)
        extension = (split_path[1]).lstrip('.')

        try:
            if extension in ('jpg', 'jpeg', 'png', 'ico'):
                self.contents = open('public{}'.format(file_path), 'rb')
            else:
                self.contents = open('public{}'.format(file_path), 'r')

            self.setContentType(extension)
            self.setStatus(200)
            return True
        except:
            self.setContentType('undefined')
            self.setStatus(404)
            return False

    def setContentType(self, ext):
        self.contentType = self.filetypes[ext]