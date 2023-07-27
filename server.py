# Copyright (C) 2023 Ibrahem Mouhamad
#
# SPDX-License-Identifier: MIT

"""
This module provides a simple HTTP server that returns system resource usage
information in JSON format. The server listens on the given address and port,
and responds to GET requests with a JSON object containing CPU, memory, network,
and disk usage information.

Usage:
The script can be run from the command line with the following arguments:
    python3 server.py [address] [port]

    [address] - the IP address or hostname to listen on (e.g., 'localhost')
    [port] - the port number to listen on (e.g., 8000)

Example:
    python3 server.py localhost 9090
"""

import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from monitor import getResourcesUsage


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        resources_usage = getResourcesUsage()
        response = json.dumps(resources_usage)
        self._set_response()
        self.wfile.write(str.encode(response))

def run(address, port, server_class=HTTPServer, handler_class=S):
    server_address = (address, port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping httpd...\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage:\n" + sys.argv[0] + " [address] [port]")
        sys.exit(1)

    run(sys.argv[1], int(sys.argv[2]))
