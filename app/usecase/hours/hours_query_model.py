from typing import List, cast

from pydantic import BaseModel, Field

from app.domain.hours import Hours


class HoursReadModel(BaseModel):
    id: str = Field(example="QK6qXDKUYf3p8x7Vb4SNas")
    user_id: str = Field(example="1")
    task_id: str = Field(example="1")
    day: str = Field(example="25/05/2021")
    minutes: int = Field(ge=0, example=150)
    note: str = Field(example="Descripcion") #TODO: Mejorar documentacion

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(hours: Hours) -> "HoursReadModel":
        return HoursReadModel(
            id=hours.id,
            user_id=hours.user_id,
            task_id=hours.task_id,
            day=hours.day,
            minutes=hours.minutes,
            note=hours.note
        )


class PaginatedHoursReadModel(BaseModel):
    hours: List[HoursReadModel] = Field(example=HoursReadModel.schema())
    count: int = Field(ge=0, example=1)
