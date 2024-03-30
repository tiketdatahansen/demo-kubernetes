import requests
import logging

logging.getLogger().setLevel(logging.DEBUG)

from fastapi import FastAPI, Request
from schema import RelayRequest

app = FastAPI()


@app.get("/echo")
async def echo(req: Request):
    return {
        "client_host": req.client.host,
        "method": req.method,
        "url": req.url._url,
        "headers": req.headers,
    }


@app.post("/relay")
async def relay(req: RelayRequest):
    logging.info(f"Relaying request: {str(req)}")

    resp = requests.request(
        req.method,
        req.url,
        headers=req.headers,
        data=req.data,
    )

    return {
        "request": {
            "url": req.url,
            "method": req.method,
            "headers": req.headers,
            "data": req.data,
        },
        "response": {
            "status": resp.status_code,
            "headers": dict(resp.headers),
            "body": resp.text,
        },
    }
