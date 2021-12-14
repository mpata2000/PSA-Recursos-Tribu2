from abc import ABC, abstractmethod
from typing import Optional

from app.domain.hours import Hours


class HoursRepository(ABC):
    @abstractmethod
    def create(self, hours: Hours) -> Optional[Hours]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Hours]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError

    @abstractmethod
    def find_existing_hours(self, day, user_id, task_id):
        raise NotImplementedError
