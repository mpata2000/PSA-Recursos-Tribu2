from abc import ABC, abstractmethod
from typing import Optional, cast

import shortuuid

from app.domain.hours import (
    Hours,
    HoursDayAlreadyExistsError,
    HoursNotFoundError,
    HoursRepository,
)
from .hours_command_model import HoursCreateModel, HoursUpdateModel
from .hours_query_model import HoursReadModel


class HoursCommandUseCaseUnitOfWork(ABC):

    hours_repository: HoursRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class HoursCommandUseCase(ABC):
    @abstractmethod
    def create_hours(
        self, data: HoursCreateModel
    ) -> Optional[HoursReadModel]:
        raise NotImplementedError

    @abstractmethod
    def update_hours(
        self, id: str, data: HoursUpdateModel
    ) -> Optional[HoursReadModel]:
        raise NotImplementedError

    @abstractmethod
    def delete_hours_by_id(self, id: str):
        raise NotImplementedError


class HoursCommandUseCaseImpl(HoursCommandUseCase):
    def __init__(
        self,
        uow: HoursCommandUseCaseUnitOfWork,
    ):
        self.uow: HoursCommandUseCaseUnitOfWork = uow

    def create_hours(
        self, data: HoursCreateModel
    ) -> Optional[HoursReadModel]:
        try:
            uuid = shortuuid.uuid()
            hours = Hours(
                id=uuid,
                user_id=data.user_id,
                task_id=data.task_id,
                day=data.day,
                minutes=data.minutes,
                note=data.note
            )

            existing_hours = self.uow.hours_repository.find_existing_hours(data.day, data.user_id)

            if existing_hours is not None:
                raise HoursDayAlreadyExistsError
            self.uow.hours_repository.create(hours)
            self.uow.commit()

            created_hours = self.uow.hours_repository.find_by_id(uuid)
        except:
            self.uow.rollback()
            raise

        return HoursReadModel.from_entity(cast(Hours, created_hours))

    def update_hours(
        self, id: str, data: HoursUpdateModel
    ) -> Optional[HoursReadModel]:
        try:
            existing_hours = self.uow.hours_repository.find_by_id(id)
            if existing_hours is None:
                raise HoursNotFoundError

            hours = Hours(
                id=id,
                user_id=existing_hours.user_id,
                day=data.day,
                minutes=data.minutes
            )

            self.uow.hours_repository.update(hours)

            updated_hours = self.uow.hours_repository.find_by_id(hours.id)

            self.uow.commit()
        except:
            self.uow.rollback()
            raise

        return HoursReadModel.from_entity(cast(Hours, updated_hours))

    def delete_hours_by_id(self, id: str):
        try:
            existing_hours = self.uow.hours_repository.find_by_id(id)
            if existing_hours is None:
                raise HoursNotFoundError

            self.uow.hours_repository.delete_by_id(id)

            self.uow.commit()
        except:
            self.uow.rollback()
            raise
