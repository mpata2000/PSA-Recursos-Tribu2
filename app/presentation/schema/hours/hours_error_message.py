from pydantic import BaseModel, Field

from app.domain.hours import (
    HoursDayAlreadyExistsError,
    HoursNotFoundError,
    HoursNotFoundError,
)
from app.domain.hours.hours_exception import CategoriesNotFoundError


class ErrorMessageHoursNotFound(BaseModel):
    detail: str = Field(example=HoursNotFoundError.message)


class ErrorMessageHoursDayAlreadyExists(BaseModel):
    detail: str = Field(example=HoursDayAlreadyExistsError.message)


class ErrorMessageHoursNotFound(BaseModel):
    detail: str = Field(example=HoursNotFoundError.message)


class ErrorMessageCategoriesNotFound(BaseModel):
    detail: str = Field(example=CategoriesNotFoundError.message)
