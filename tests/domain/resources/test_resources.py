import pytest

from app.domain.resources import Resources


class TestResources:
    def test_constructor_should_create_instance(self):
        resources = Resources(
            legajo="106226",
            Nombre="Martin",
            Apellido="Pata",
        )

        assert resources.legajo == "106226"
        assert resources.Nombre == "Martin"
        assert resources.Apellido == "Pata"

    def test_resource_entity_should_be_identified_by_id(self):
        resources1 = Resources(
            legajo="106226",
            Nombre="Martin",
            Apellido="Pata",
        )

        resources2 = Resources(
            legajo="106226",
            Nombre="Martin",
            Apellido="Fraile",
        )

        resources3 = Resources(
            legajo="106",
            Nombre="Juampi",
            Apellido="Di Como",
        )

        assert resources1 == resources2
        assert resources1 != resources3
