from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from core.infra.errors.generic_error import GenericError


class ErrorResponse(BaseModel):
    status: int
    detail: str
    code: str
    title: str


async def generic_error_handler(request: Request, err: GenericError):
    status_code = err.status_code
    titles = {
        400: "400: Bad Request",
        401: "401 Unauthorized",
        403: "403: Forbidden",
        404: "404: Not Found",
        405: "405: Method Not Allowed",
        500: "500: Internal Server Error",
    }
    title = titles.get(status_code)
    error = ErrorResponse(
        status=status_code, code=err.code_error, detail=err.message, title=title
    )

    content = error.model_dump()

    return JSONResponse(status_code=status_code, content=content)


async def internal_server_error_handler(request: Request, err: Exception):
    exc_class = GenericError(
        message="An error has ocourred, contact the suport.",
        code_error="INTERNAL_SERVER_ERROR",
        status_code=500,
    )
    return await generic_error_handler(request=request, err=exc_class)


async def not_found_handler(request: Request, err: Exception):
    exc_class = GenericError(
        message="Url not found.", code_error="URL_NOT_FOUND", status_code=404
    )
    return await generic_error_handler(request=request, err=exc_class)
