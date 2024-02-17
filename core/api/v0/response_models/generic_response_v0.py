from typing import Any, Dict, Generic, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class GenericResponseV0(BaseModel, Generic[T]):
    message: str = ""
    meta: Optional[Dict[str, Any]] = {}
    data: Optional[T] = None
