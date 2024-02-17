from core.infra.errors.generic_error import GenericError


class NotFound(GenericError):
    def __init__(self, message, code_error="ANY") -> None:
        status_code = 404
        super().__init__(message, code_error, status_code)
