from typing import Optional
from datetime import date


class Hours:
    def __init__(
        self,
        id: str,
        user_id: str,
        task_id: str,
        day: date,
        hours: int,
        minutes: int,
        seconds: int,
        note: Optional[str] = None,
    ):
        self.id: str = id
        self.user_id: str = user_id
        self.task_id: str = task_id
        self.day: date = day
        self.hours: int = hours
        self.minutes: int = minutes
        self.seconds: int = seconds
        self.note: Optional[str] = note

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Hours):
            return self.id == o.id

        return False
