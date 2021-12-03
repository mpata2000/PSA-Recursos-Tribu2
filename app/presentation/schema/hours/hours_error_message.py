from pydantic import BaseModel, Field

from app.domain.hours import (
    HoursDayAlreadyExistsError,
    HoursNotFoundError,
)



class ErrorMessageHoursNotFound(BaseModel):
    detail: str = Field(example=HoursNotFoundError.message)


class ErrorMessageHoursDayAlreadyExists(BaseModel):
    detail: str = Field(example=HoursDayAlreadyExistsError.message)

class ErrorMessageResourcesNotFound(BaseModel):
    detail: str = Field(example="ResourcesNotFound")


class ErrorMessageHoursNotFound(BaseModel):
    detail: str = Field(example=HoursNotFoundError.message)
