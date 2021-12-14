from typing import List
from pydantic import BaseModel, Field
from app.domain.resources import Resources


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
