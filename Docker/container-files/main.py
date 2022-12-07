#!/usr/bin/env python3
import time
from http.server import HTTPServer
from server import Server

HOSTNAME = ''
PORT_NUMBER = 8080

if __name__ == '__main__':
    httpd = HTTPServer((HOSTNAME, PORT_NUMBER), Server)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOSTNAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOSTNAME, PORT_NUMBER))