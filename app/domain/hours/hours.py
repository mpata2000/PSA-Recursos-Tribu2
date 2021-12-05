from typing import List, Optional
from datetime import date


class Hours:
    def __init__(
        self,
        id: str,
        user_id: str,
        task_id: str,
        day: date,
        minutes: int,
        note: Optional[str] = None,
    ):
        self.id: str = id
        self.user_id: str = user_id
        self.task_id: str = task_id
        self.day: date = day
        self.minutes: int = minutes
        self.note: str = note

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Hours):
            return self.id == o.id

        return False
