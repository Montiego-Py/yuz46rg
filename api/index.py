import json
import requests
from urllib.parse import parse_qs, urlparse

def handler(request):
    try:
        # Query string al
        parsed = urlparse(request.url)
        query = parse_qs(parsed.query)

        target_url = query.get("url", [None])[0]
        method = query.get("method", ["GET"])[0]
        headers = json.loads(query.get("headers", ["{}"])[0])
        payload = query.get("payload", [None])[0]

        if not target_url:
            return {
                "statusCode": 400,
                "body": "URL eksik!"
            }

        res = requests.request(
            method=method,
            url=target_url,
            headers=headers,
            data=payload,
            timeout=15
        )

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "status_code": res.status_code,
                "body": res.text
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
