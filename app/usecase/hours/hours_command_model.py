from typing import List

from pydantic import BaseModel, Field


class HoursCreateModel(BaseModel):
    user_id: str = Field(example="1")
    task_id: str = Field(example="1")
    day: str = Field(example="25/05/2021")
    minutes: int = Field(ge=0, example=150)
    note: str = Field(example="Descripcion") #TODO: Mejorar documentacion


class HoursUpdateModel(BaseModel):
    task_id: str = Field(example="1")
    day: str = Field(example="25/05/2021")
    minutes: int = Field(ge=0, example=150)
