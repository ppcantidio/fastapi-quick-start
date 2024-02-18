import logging
from copy import copy
from typing import Any

from asgi_correlation_id import correlation_id
from logtail import LogtailHandler

from config import settings


class CloudLoggingHandler(LogtailHandler):
    def __init__(self):
        super().__init__(settings("LOGTAIL_SOURCE_TOKEN"))

    def emit(self, record: Any):
        log = copy(record)
        if hasattr(log, "_logger"):
            delattr(log, "_logger")
        if hasattr(log, "_name"):
            delattr(log, "_name")
        log.request_id = correlation_id.get()
        return super().emit(log)
