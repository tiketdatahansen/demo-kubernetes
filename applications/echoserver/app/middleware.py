import json
import logging
from datetime import datetime

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.concurrency import iterate_in_threadpool


logger = logging.getLogger()


class HTTPLogger(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        req_body = await request.body()
        logger.info(
            json.dumps(
                {
                    "type": "http_request",
                    "method": request.method,
                    "endpoint": request.url.path,
                    "clientIp": request.client,
                    "hostIp": request.headers.get("host"),
                    "timestamp": datetime.now().__str__(),
                    "httpStatus": None,
                    "content": req_body.decode("utf8"),
                }
            )
        )

        response = await call_next(request)
        resp_body = [chunk async for chunk in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(resp_body))
        logger.info(
            json.dumps(
                {
                    "type": "http_response",
                    "method": request.method,
                    "endpoint": request.url.path,
                    "clientIp": request.client,
                    "hostIp": request.headers.get("host"),
                    "timestamp": datetime.now().__str__(),
                    "httpStatus": response.status_code,
                    "content": b"".join(resp_body).decode("utf8"),
                }
            )
        )

        return response
