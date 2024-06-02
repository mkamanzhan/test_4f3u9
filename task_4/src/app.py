from fastapi import FastAPI

from src.api.setup import setup_routes


def get_app() -> FastAPI:
    app = FastAPI(
        title="Task 4",
    )
    setup_routes(app)
    return app
