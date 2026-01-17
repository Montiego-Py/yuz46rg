from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        response = {
            "message": "Python Vercel function çalışıyor 🚀"
        }

        self.wfile.write(json.dumps(response).encode())
