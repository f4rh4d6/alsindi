import http.server
import socketserver
import json
import os
import sys
import base64
import re
import datetime

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADMIN_USER = "Admin"
ADMIN_PASS = "Admin"

class AdminAPIHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, *args):
        pass

    def _is_authenticated(self):
        auth_header = self.headers.get('Authorization')
        if not auth_header:
            return False
        try:
            auth_type, encoded = auth_header.split(' ', 1)
            if auth_type.lower() != 'basic':
                return False
            decoded = base64.b64decode(encoded).decode('utf-8')
            username, password = decoded.split(':', 1)
            return username == ADMIN_USER and password == ADMIN_PASS
        except Exception:
            return False

    def _require_auth(self):
        if not self._is_authenticated():
            self.send_response(401)
            self.send_header('WWW-Authenticate', 'Basic realm="Admin Access Required"')
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b"<h1>401 Unauthorized - Admin Login Required</h1>")
            return False
        return True

    def do_GET(self):
        # Require authentication to view admin.html or /admin
        clean_path = self.path.split('?')[0]
        if clean_path in ('/admin.html', '/admin'):
            if not self._require_auth():
                return

        if self.path == '/api/data':
            self._handle_get_data()
        elif self.path == '/api/images':
            self._handle_get_images()
        elif self.path == '/api/inquiries':
            if not self._require_auth():
                return
            self._handle_get_inquiries()
        else:
            super().do_GET()

    def _handle_get_data(self):
        try:
            with open(os.path.join(DIRECTORY, 'assets', 'js', 'data.js'), 'r', encoding='utf-8') as f:
                content = f.read()
                start = content.find('{')
                end = content.rfind('}')
                if start != -1 and end != -1:
                    json_str = content[start:end+1]
                    data = json.loads(json_str)
                    self._send_json(data)
                    return
        except Exception as e:
            self._send_error(str(e))
            return
        self.send_error(404, "Data not found")

    def _handle_get_images(self):
        img_dir = os.path.join(DIRECTORY, 'assets', 'images')
        os.makedirs(img_dir, exist_ok=True)
        images = []
        if os.path.exists(img_dir):
            for f in os.listdir(img_dir):
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')):
                    images.append(f'assets/images/{f}')
        self._send_json({"images": sorted(images)})

    def _handle_get_inquiries(self):
        inq_file = os.path.join(DIRECTORY, 'inquiries.json')
        data = []
        if os.path.exists(inq_file):
            try:
                with open(inq_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except Exception:
                pass
        self._send_json({"inquiries": data})

    def do_POST(self):
        if self.path == '/api/save':
            if not self._require_auth():
                return
            self._handle_save()
        elif self.path == '/api/upload':
            if not self._require_auth():
                return
            self._handle_upload()
        elif self.path == '/api/inquiry':
            self._handle_post_inquiry()
        elif self.path == '/api/save-css':
            if not self._require_auth():
                return
            self._handle_save_css()
        else:
            self.send_error(404, "Endpoint not found")

    def _handle_save(self):
        data = self._read_json_payload()
        if data is None: return

        data_path = os.path.join(DIRECTORY, 'assets', 'js', 'data.js')
        # Backup
        try:
            backup_dir = os.path.join(DIRECTORY, 'backups')
            os.makedirs(backup_dir, exist_ok=True)
            ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            if os.path.exists(data_path):
                with open(data_path, 'r', encoding='utf-8') as src:
                    with open(os.path.join(backup_dir, f'data_{ts}.js'), 'w', encoding='utf-8') as dst:
                        dst.write(src.read())
        except Exception:
            pass

        js_content = f"""/* ============================================================
   THE SURVEY — Portfolio Data Store
   Single source of truth for site content & photography catalog.
   ============================================================ */

const DEFAULT_SITE_DATA = {json.dumps(data, indent=2)};

function getSiteData() {{
  return DEFAULT_SITE_DATA;
}}
"""
        try:
            with open(data_path, 'w', encoding='utf-8') as f:
                f.write(js_content)
            self._send_json({"success": True})
        except Exception as e:
            self._send_error(str(e))

    def _handle_upload(self):
        payload = self._read_json_payload()
        if not payload: return

        filename = payload.get('filename', 'upload.jpg')
        filedata = payload.get('filedata', '')

        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = re.sub(r'[^a-zA-Z0-9.-]', '_', filename)
        new_filename = f"up_{ts}_{safe_name}"

        if ',' in filedata:
            filedata = filedata.split(',')[1]

        try:
            decoded = base64.b64decode(filedata)
            os.makedirs(os.path.join(DIRECTORY, 'assets', 'images'), exist_ok=True)
            filepath = os.path.join(DIRECTORY, 'assets', 'images', new_filename)
            with open(filepath, 'wb') as f:
                f.write(decoded)
            self._send_json({"success": True, "path": f"assets/images/{new_filename}"})
        except Exception as e:
            self._send_error(str(e))

    def _handle_save_css(self):
        payload = self._read_json_payload()
        if not payload: return

        filename = payload.get('filename', 'design_overrides.css')
        content  = payload.get('content', '')

        # Only allow writing CSS files to the site directory
        safe_name = re.sub(r'[^a-zA-Z0-9_.-]', '_', os.path.basename(filename))
        if not safe_name.endswith('.css'):
            self._send_error('Only .css files are allowed', 400)
            return

        css_path = os.path.join(DIRECTORY, safe_name)
        try:
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(content)

            # Inject the override <link> into every .html page if not already present
            link_tag = f'<link rel="stylesheet" href="{safe_name}">'
            for html_file in ['index.html', 'gallery.html', 'about.html',
                              'commentary.html', 'contact.html']:
                html_path = os.path.join(DIRECTORY, html_file)
                if not os.path.exists(html_path):
                    continue
                with open(html_path, 'r', encoding='utf-8') as f:
                    html = f.read()
                if link_tag not in html:
                    # Insert just before </head>
                    html = html.replace('</head>', f'  {link_tag}\n</head>', 1)
                    with open(html_path, 'w', encoding='utf-8') as f:
                        f.write(html)

            self._send_json({"success": True, "path": safe_name})
        except Exception as e:
            self._send_error(str(e))

    def _handle_post_inquiry(self):
        inquiry = self._read_json_payload()
        if not inquiry: return

        inquiry['timestamp'] = datetime.datetime.now().isoformat()

        inq_file = os.path.join(DIRECTORY, 'inquiries.json')
        data = []
        if os.path.exists(inq_file):
            try:
                with open(inq_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except Exception:
                pass

        data.insert(0, inquiry)
        try:
            with open(inq_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            self._send_json({"success": True})
        except Exception as e:
            self._send_error(str(e))

    def _read_json_payload(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length == 0:
                self.send_response(400)
                self.end_headers()
                return None
            body = self.rfile.read(content_length).decode('utf-8')
            return json.loads(body)
        except Exception as e:
            self._send_error(f"Payload error: {str(e)}", 400)
            return None

    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def _send_error(self, message, status=500):
        self._send_json({"error": message}, status)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

# Allow terminating old servers to free up port
socketserver.TCPServer.allow_reuse_address = True
try:
    with socketserver.TCPServer(("", PORT), AdminAPIHandler) as httpd:
        print(f"Serving Advanced Admin Backend on http://localhost:{PORT}", flush=True)
        httpd.serve_forever()
except OSError as e:
    print(f"Port {PORT} might be in use: {e}", file=sys.stderr)
