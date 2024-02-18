import copy
from typing import Any

from logtail import LogtailHandler

from config import settings


class LoggingHandler(LogtailHandler):
    def __init__(self):
        super().__init__(settings("LOGTAIL_SOURCE_TOKEN"))

    def emit(self, record: Any):
        log = copy(record)
        if hasattr(log, "_logger"):
            delattr(log, "_logger")
        if hasattr(log, "_name"):
            delattr(log, "_name")
        return super().emit(log)
