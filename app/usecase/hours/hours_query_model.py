from typing import List, cast

from pydantic import BaseModel, Field

from app.domain.hours import Hours


class HoursReadModel(BaseModel):

    id: str = Field(example="vytxeTZskVKR7C7WgdSP3d")
    user_id: str = Field(example="a2s1daxeTZsgdSP3d")
    day: str = Field(example="25/05/2021")
    minutes: int = Field(ge=0, example=10)

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(hours: Hours) -> "HoursReadModel":
        return HoursReadModel(
            id=hours.id,
            user_id=hours.user_id,
            day=hours.day,
            minutes=hours.minutes
        )


class PaginatedHoursReadModel(BaseModel):
    hours: List[HoursReadModel] = Field(example=HoursReadModel.schema())
    count: int = Field(ge=0, example=1)
