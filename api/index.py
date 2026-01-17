from fastapi import FastAPI, Request
import httpx

app = FastAPI()

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy(request: Request, path: str):
    # url param bekle
    url = request.query_params.get("url")
    if not url:
        return {"error": "url query param is required"}

    # headers ve method
    headers = dict(request.headers)
    method = request.method

    async with httpx.AsyncClient() as client:
        res = await client.request(method, url, headers=headers, content=await request.body())

    return {
        "status_code": res.status_code,
        "body": res.text
    }
