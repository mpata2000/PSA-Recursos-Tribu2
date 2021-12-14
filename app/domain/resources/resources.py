
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
            return self.legajo == o.legajo

        return False
