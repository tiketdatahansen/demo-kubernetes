from uuid import uuid4
import logging
import requests

from fastapi import APIRouter, Request

from schema import RelayRequest
from version import VERSION


router = APIRouter()
ID = str(uuid4())


@router.get("/id")
async def id():
    return {"id": ID}


@router.get("/version")
async def version():
    return {"version": VERSION}


@router.get("/echo")
async def echo(req: Request):
    return {
        "client_host": req.client.host,
        "method": req.method,
        "url": req.url._url,
        "headers": req.headers,
    }


@router.post("/relay")
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
