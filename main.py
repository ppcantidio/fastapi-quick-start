import uvicorn
from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import setup_logging
from core.api.v0.routes import add_routers_v0
from core.infra.errors import BadRequest, Forbidden, NotFound, Unauthorized
from core.infra.handlers import errors_handlers
from core.infra.middlewares.logging_middleware import LoggingMiddleware


def add_routers(app: FastAPI):
    add_routers_v0(app)


def add_middlewares(app: FastAPI):
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(CorrelationIdMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def add_handdlers(app: FastAPI):
    app.add_exception_handler(400, errors_handlers.not_found_handler)
    app.add_exception_handler(500, errors_handlers.internal_server_error_handler)
    app.add_exception_handler(BadRequest, errors_handlers.generic_error_handler)
    app.add_exception_handler(NotFound, errors_handlers.generic_error_handler)
    app.add_exception_handler(Forbidden, errors_handlers.generic_error_handler)
    app.add_exception_handler(Unauthorized, errors_handlers.generic_error_handler)


def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(title="Example API", version="1.0.0")

    add_middlewares(app)
    add_handdlers(app)
    add_routers(app)

    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="127.0.0.1", port=8000, log_config=None)
