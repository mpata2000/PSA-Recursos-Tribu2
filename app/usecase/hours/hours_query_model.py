from datetime import date
from typing import List

from pydantic import BaseModel, Field

from app.domain.hours import Hours


class HoursReadModel(BaseModel):
    id: str = Field(example="QK6qXDKUYf3p8x7Vb4SNas")
    user_id: str = Field(example="1")
    task_id: str = Field(example="1")
    day: date = Field(example="2021-05-25")
    hours: int = Field(ge=0, le=23, example=3)
    minutes: int = Field(ge=0, le=59, example=45)
    seconds: int = Field(ge=0, le=59, example=10)
    note: str = Field(example="Descripcion")

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(hours: Hours) -> "HoursReadModel":
        return HoursReadModel(
            id=hours.id,
            user_id=hours.user_id,
            task_id=hours.task_id,
            day=hours.day,
            hours=hours.hours,
            minutes=hours.minutes,
            seconds=hours.seconds,
            note=hours.note
        )


class PaginatedHoursReadModel(BaseModel):
    hours: List[HoursReadModel] = Field(example=HoursReadModel.schema())
    count: int = Field(ge=0, example=1)
