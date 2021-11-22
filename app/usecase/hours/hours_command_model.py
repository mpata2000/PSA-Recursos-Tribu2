from typing import List

from pydantic import BaseModel, Field


class HoursCreateModel(BaseModel):

    day: str = Field(example="25/05/2021")
    minutes: int = Field(ge=0, example=150)


class HoursUpdateModel(BaseModel):

    day: str = Field(example="25/05/2021")
    minutes: int = Field(ge=0, example=150)
