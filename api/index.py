from http.server import BaseHTTPRequestHandler
import requests
import json
from urllib.parse import parse_qs, urlparse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        
        target_url = query.get('url', [None])[0]
        method = query.get('method', ['GET'])[0]
        headers = json.loads(query.get('headers', ['{}'])[0])
        payload = query.get('payload', [None])[0]

        if not target_url:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"URL eksik!")
            return

        try:
            # İsteği hedefe gönder
            res = requests.request(
                method=method,
                url=target_url,
                headers=headers,
                data=payload,
                timeout=30,
                verify=False # SSL hatalarını görmezden gel
            )

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response_data = {
                "status_code": res.status_code,
                "body": res.text
            }
            self.wfile.write(json.dumps(response_data).encode())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())
