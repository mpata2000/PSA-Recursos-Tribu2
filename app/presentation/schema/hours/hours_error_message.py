from pydantic import BaseModel, Field

from app.domain.hours import (
    HoursDayAlreadyExistsError,
    HoursNotFoundError,
    HoursNotValidDateError,
)


class ErrorMessageHoursNotFound(BaseModel):
    detail: str = Field(example=HoursNotFoundError.message)


class ErrorMessageHoursDayAlreadyExists(BaseModel):
    detail: str = Field(example=HoursDayAlreadyExistsError.message)


class ErrorMessageHoursNotValidDate(BaseModel):
    detail: str = Field(example=HoursNotValidDateError.message)
