from datetime import date
from typing import List

from pydantic import BaseModel, Field


class HoursCreateModel(BaseModel):
    user_id: str = Field(example="1")
    task_id: str = Field(example="1")
    day: date = Field(example="2021-05-25")
    minutes: int = Field(ge=0, example=150)
    note: str = Field(example="Descripcion")


class HoursPutModel(BaseModel):
    day: date = Field(example="2021-05-25")
    minutes: int = Field(ge=0, example=150)
    note: str = Field(example="Descripcion")
