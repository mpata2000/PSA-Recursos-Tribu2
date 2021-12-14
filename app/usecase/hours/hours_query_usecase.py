from abc import ABC, abstractmethod
from datetime import date
from typing import List, Optional, Tuple

from app.domain.hours import HoursNotFoundError
from app.usecase.hours.hours_query_model import HoursReadModel

from .hours_query_service import HoursQueryService


class HoursQueryUseCase(ABC):
    @abstractmethod
    def fetch_hours_by_id(self, id: str) -> Optional[HoursReadModel]:
        raise NotImplementedError

    @abstractmethod
    def fetch_hours(
        self, limit: int = 100, offset: int = 0
    ) -> Tuple[List[HoursReadModel], int]:
        raise NotImplementedError


    @abstractmethod
    def fetch_hours_by_filters(
        self,
        ids: Optional[List[str]],
        day: Optional[date],
        user_id: Optional[str],
        task_id: Optional[str],
        minutes: Optional[int],
        limit: int = 100,
        offset: int = 0,
    ) -> Tuple[List[HoursReadModel], int]:
        raise NotImplementedError



class HoursQueryUseCaseImpl(HoursQueryUseCase):
    def __init__(self, hours_query_service: HoursQueryService):
        self.hours_query_service: HoursQueryService = hours_query_service

    def fetch_hours_by_id(self, id: str) -> Optional[HoursReadModel]:
        try:
            hours = self.hours_query_service.find_by_id(id)
            if hours is None:
                raise HoursNotFoundError
        except:
            raise

        return hours

    def fetch_hours(
        self, limit: int = 100, offset: int = 0
    ) -> Tuple[List[HoursReadModel], int]:
        try:
            hours, count = self.hours_query_service.find_all(
                limit=limit, offset=offset
            )
        except:
            raise

        return hours, count

    def fetch_hours_by_filters(
        self,
        ids: Optional[List[str]],
        day: Optional[date],
        user_id: Optional[str],
        task_id: Optional[str],
        minutes: Optional[int],
        limit: int = 100,
        offset: int = 0,
    ) -> Tuple[List[HoursReadModel], int]:
        try:
            hours, count = self.hours_query_service.find_by_filters(
                ids=ids,
                day=day,
                user_id=user_id,
                task_id=task_id,
                minutes=minutes,
                limit=limit,
                offset=offset
            )
        except:
            raise

        return hours, count
