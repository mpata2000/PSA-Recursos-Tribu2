from abc import ABC, abstractmethod
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
        day: Optional[str],
        user_id: Optional[str],
        task_id: Optional[str],
        minutes:Optional[int],
        limit: int = 100,
        offset: int = 0,
    ) -> Tuple[List[HoursReadModel], int]:
        raise NotImplementedError
