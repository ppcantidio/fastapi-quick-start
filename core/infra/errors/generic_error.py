class GenericError(Exception):
    def __init__(self, message, code_error, status_code: int) -> None:
        self.code_error = code_error
        self.message = message
        self.status_code = status_code

        super().__init__(message)
