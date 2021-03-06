from datetime import datetime, date
from typing import Union

from sqlalchemy import Column, String, Date, Integer

from app.domain.hours import Hours
from app.infrastructure.database import Base
from app.usecase.hours import HoursReadModel


def unixtimestamp() -> int:
    return int(datetime.now().timestamp() * 1000)


class HoursDTO(Base):

    __tablename__ = "hours"
    id: Union[str, Column] = Column(String, primary_key=True, autoincrement=False)
    user_id: Union[str, Column] = Column(String, nullable=False, autoincrement=False)
    task_id: Union[str, Column] = Column(String, nullable=False, autoincrement=False)
    day: Union[date, Column] = Column(Date, nullable=False, autoincrement=False)
    hours: Union[int, Column] = Column(Integer, nullable=False)
    minutes: Union[int, Column] = Column(Integer, nullable=False)
    seconds: Union[int, Column] = Column(Integer, nullable=False)
    note: Union[str, Column] = Column(String, nullable=True)

    def to_entity(self) -> Hours:
        return Hours(
            id=self.id,
            user_id=self.user_id,
            task_id=self.task_id,
            day=self.day,
            hours=self.hours,
            minutes=self.minutes,
            seconds=self.seconds,
            note=self.note
        )

    def to_read_model(self) -> HoursReadModel:
        return HoursReadModel(
            id=self.id,
            user_id=self.user_id,
            task_id=self.task_id,
            day=self.day,
            hours=self.hours,
            minutes=self.minutes,
            seconds=self.seconds,
            note=self.note
        )

    @staticmethod
    def from_entity(hours: Hours) -> "HoursDTO":
        return HoursDTO(
            id=hours.id,
            user_id=hours.user_id,
            task_id=hours.task_id,
            day=hours.day,
            hours=hours.hours,
            minutes=hours.minutes,
            seconds=hours.seconds,
            note=hours.note
        )
