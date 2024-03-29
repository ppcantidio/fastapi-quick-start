import logging
import time

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from uvicorn.protocols.utils import get_path_with_query_string

access_logger = logging.getLogger("access")


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware class for logging HTTP requests and responses.

    This middleware logs the details of incoming HTTP requests and outgoing responses,
    including the request method, URL, status code, client IP address, and processing time.

    Methods:
        dispatch(request: Request, call_next: RequestResponseEndpoint) -> Response:
            Dispatches the request to the next middleware or endpoint, and logs the details
            of the request and response.

    """

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        response = Response(status_code=500)

        start_time = time.perf_counter_ns()
        try:
            response = await call_next(request)
        except Exception:
            logging.getLogger("core").exception("Uncaught exception")
            raise
        finally:
            process_time = time.perf_counter_ns() - start_time

            status_code = response.status_code
            url = get_path_with_query_string(request.scope)
            client_host = request.client.host
            client_port = request.client.port
            http_method = request.method
            http_version = request.scope["http_version"]

            access_logger.info(
                f"""{client_host}:{client_port} - "{http_method} {url} HTTP/{http_version}" {status_code}""",
                extra={
                    "http": {
                        "url": str(request.url),
                        "status_code": status_code,
                        "method": http_method,
                        "version": http_version,
                    },
                    "network": {"client": {"ip": client_host, "port": client_port}},
                    "duration": process_time,
                },
            )
            response.headers["X-Process-Time"] = str(process_time / 10**9)
            return response
