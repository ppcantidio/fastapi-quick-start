from datetime import datetime

from pydantic import BaseModel


class HealthResponseV0(BaseModel):
    api_version: str
    time: datetime
    status: str
