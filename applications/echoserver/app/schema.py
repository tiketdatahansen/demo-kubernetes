from enum import Enum
from typing import Optional
from pydantic import BaseModel


class HttpMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"
    PATCH = "PATCH"


class RelayRequest(BaseModel):
    url: str = "http://localhost:8000"
    method: HttpMethod = HttpMethod.GET
    headers: dict = {}
    data: Optional[str] = None
