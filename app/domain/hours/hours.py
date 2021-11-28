from typing import List, Optional
from datetime import date


class Hours:
    def __init__(
        self,
        id: str,
        user_id: str,
        task_id: str,
        day: str,
        minutes: int,
        note: str,
    ):
        self.id: str = id
        self.user_id: str = user_id
        self.task_id: str = task_id
        self.day: str = day
        self.minutes: int = minutes
        self.note: str = note

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Hours):
            return self.id == o.id

        return False
