import structlog


class LoggerAdapter:
    @classmethod
    def get_logger(cls, logger_name: str) -> structlog.BoundLogger:
        logger = structlog.stdlib.get_logger(logger_name)
        return logger
