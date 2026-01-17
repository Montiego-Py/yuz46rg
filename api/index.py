import requests
import json

def handler(request):
    # query ile target al
    params = request.query
    target = params.get("url")
    method = params.get("method", "GET").upper()

    if not target:
        return {
            "statusCode": 400,
            "body": "URL parametresi gerekli"
        }

    try:
        # veri alma (POST vs.)
        body = None
        if method in ["POST","PUT","PATCH"]:
            body = request.body

        res = requests.request(
            method,
            target,
            headers=dict(request.headers),
            data=body,
            timeout=15
        )

        return {
            "statusCode": res.status_code,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "status": res.status_code,
                "data": res.text
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Proxy error: {str(e)}"
        }
