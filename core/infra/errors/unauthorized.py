from core.infra.errors.generic_error import GenericError


class Unauthorized(GenericError):
    def __init__(self, message, code_error="ANY") -> None:
        status_code = 401
        super().__init__(message, code_error, status_code)
