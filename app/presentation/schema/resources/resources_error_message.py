from pydantic import BaseModel, Field

from app.domain.resources import (
    ResourcesNotFoundError,
)

class ErrorMessageResourcesNotFound(BaseModel):
    detail: str = Field(example=ResourcesNotFoundError.message)
