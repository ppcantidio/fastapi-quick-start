from core.infra.errors.generic_error import GenericError


class Forbidden(GenericError):
    def __init__(self, message, code_error="ANY") -> None:
        status_code = 403
        super().__init__(message, code_error, status_code)
