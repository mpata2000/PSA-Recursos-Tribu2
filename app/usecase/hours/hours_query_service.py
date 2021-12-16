from abc import ABC, abstractmethod
from datetime import date
from typing import List, Optional, Tuple

from app.usecase.hours.hours_query_model import HoursReadModel


class HoursQueryService(ABC):
    @abstractmethod
    def find_by_id(self, id: str) -> Optional[HoursReadModel]:
        raise NotImplementedError

    @abstractmethod
    def find_all(
        self, limit: int = 100, offset: int = 0
    ) -> Tuple[List[HoursReadModel], int]:
        raise NotImplementedError

    @abstractmethod
    def find_by_filters(
        self,
        ids: Optional[List[str]],
        day: Optional[date],
        user_id: Optional[str],
        task_id: Optional[str],
        limit: int = 100,
        offset: int = 0,
    ) -> Tuple[List[HoursReadModel], int]:
        raise NotImplementedError
