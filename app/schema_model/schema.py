from typing import Optional

from pydantic import BaseModel, Field


class RequestModel(BaseModel):
    """
    A pydantic model to validate input request body
    """
    query: str = Field(..., min_length=1)
    top_k: Optional[int] = Field(2, gt=0, lt=1000)
