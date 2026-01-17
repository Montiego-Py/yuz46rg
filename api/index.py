from fastapi import FastAPI, Request
import httpx

app = FastAPI()

@app.get("/")  # /api/proxy
async def proxy(request: Request, url: str = None):
    if not url:
        return {"error": "url query param missing"}

    # Gelen query ve headers ile hedef siteye getir
    headers = dict(request.headers)
    async with httpx.AsyncClient() as client:
        res = await client.get(url, headers=headers)

    return {"status_code": res.status_code, "content": res.text}
