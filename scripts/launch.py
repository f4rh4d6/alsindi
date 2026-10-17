#!/usr/bin/env python3
"""Portfolio server that works within sandbox restrictions.

Serves all site assets from a pinned working directory to avoid issues
with os.getcwd() in the sandbox.
"""
import http.server
import socketserver
import os

PORT = 8000
WORK_DIR = "/Users/alsindi/Desktop/website"

class NoCwdHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WORK_DIR, **kwargs)

    def log_message(self, *args):
        pass

with socketserver.TCPServer(("", PORT), NoCwdHandler) as httpd:
    httpd.allow_reuse_address = True
    print(f"Serving {WORK_DIR} on http://localhost:{PORT}", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("Server stopped.", flush=True)