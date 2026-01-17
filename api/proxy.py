from fastapi import FastAPI, Request
import httpx

app = FastAPI()

@app.get("/")
async def proxy(request: Request, url: str = None):
    if not url:
        return {"error": "url param gerekli"}

    # header’ları hedefe geçir
    headers = dict(request.headers)

    # httpx ile GET isteği yap
    async with httpx.AsyncClient() as client:
        res = await client.get(url, headers=headers)

    return {
        "status_code": res.status_code,
        "body": res.text
    }
