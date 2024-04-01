import os
import logging

logging.getLogger().setLevel(logging.DEBUG)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)-15s %(levelname)s - %(message)s"
)

from fastapi import FastAPI
from fastapi.middleware import Middleware

from middleware import HTTPLogger
from router import router
from version import VERSION

root_path = os.getenv("ROOT_PATH", "/").rstrip("/")
logging.info(f"Root path: '{root_path}'")

app = FastAPI(
    version=VERSION,
    middleware=[Middleware(HTTPLogger)],
    openapi_url=f"{root_path}/openapi.json",
    docs_url=f"{root_path}/docs",
)
app.include_router(router, prefix=root_path)
