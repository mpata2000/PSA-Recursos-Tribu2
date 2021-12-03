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


class Resources:
    def __init__(
            self,
            legajo: str,
            Nombre: str,
            Apellido: str,
    ):
        self.legajo: str = legajo
        self.Nombre: str = Nombre
        self.Apellido: str = Apellido

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Resources):
            return self.id == o.id

        return False


class ResourcesReadModel(BaseModel):
    legajo: str = Field(example="123123")
    Nombre: str = Field(example="Mendez")
    Apellido: str = Field(example="Argerich")

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(resources: Resources) -> "ResourcesReadModel":
        return ResourcesReadModel(
            legajo=resources.legajo,
            Nombre=resources.Nombre,
            Apellido=resources.Apellido,

        )

class PaginatedResourcesReadModel(BaseModel):
    resources: List[ResourcesReadModel] = Field(example=ResourcesReadModel.schema())
    count: int = Field(ge=0, example=1)
