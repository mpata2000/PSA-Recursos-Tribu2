from typing import List, Optional


class Hours:
    def __init__(
        self,
        id: str,
        user_id: str,
        day: str,
        minutes: int,
    ):
        self.id: str = id
        self.user_id: str = user_id
        self.day: str = day
        self.minutes: int = minutes

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Hours):
            return self.id == o.id

        return False
