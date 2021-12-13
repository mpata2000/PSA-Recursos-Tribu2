from pydantic import BaseModel, Field

from app.domain.hours import (
    HoursDayAlreadyExistsError,
    HoursNotFoundErrorInDate,
    HoursNotFoundError,
    HoursNotValidDateError,
)



class ErrorMessageHoursNotFound(BaseModel):
    detail: str = Field(example=HoursNotFoundError.message)


class ErrorMessageHoursDayAlreadyExists(BaseModel):
    detail: str = Field(example=HoursDayAlreadyExistsError.message)


class ErrorMessageHoursNotFoundInDate(BaseModel):
    detail: str = Field(example=HoursNotFoundErrorInDate.message)


class ErrorMessageHoursNotValidDate(BaseModel):
    detail: str = Field(example=HoursNotValidDateError.message)
