from pydantic import BaseModel
from typing import Any, Optional
from datetime import datetime


class ResponseModel(BaseModel):
    status_code: int
    message: str
    data: Optional[Any] = None
    error_code: Optional[str] = None
    timestamp: str
    success: bool

    @classmethod
    def create_response(cls, status_code: int, message: str, data: Any = None, error_code: str = None, success: bool = True):
        return cls(
            status_code=status_code,
            message=message,
            data=data,
            error_code=error_code,
            timestamp=datetime.now().isoformat(),
            success=success
        )
