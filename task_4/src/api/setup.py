from fastapi import FastAPI

from src.api.content import router as content_router
from src.api.health import router as health_router


def setup_routes(app: FastAPI) -> None:
    app.include_router(health_router)
    app.include_router(content_router)
