from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class HoursCreateModel(BaseModel):
    user_id: str = Field(example="1")
    task_id: str = Field(example="1")
    day: date = Field(example="2021-05-25")
    hours: int = Field(ge=0, le=23, example=3)
    minutes: int = Field(ge=0, le=59, example=45)
    seconds: int = Field(ge=0, le=59, example=10)
    note: str = Field(example="Descripcion")


class HoursPatchModel(BaseModel):
    user_id: Optional[str]  = Field(example="1")
    task_id: Optional[str]  = Field(example="1")
    day: Optional[date] = Field(example="2021-05-25")
    hours: Optional[int] = Field(ge=0, le=23, example=3)
    minutes: Optional[int] = Field(ge=0, le=59, example=45)
    seconds: Optional[int] = Field(ge=0, le=59, example=10)
    note: Optional[str] = Field(example="Descripcion")
