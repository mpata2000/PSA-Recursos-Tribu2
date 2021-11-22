from datetime import datetime
from typing import Union
from app.domain.hours import Hours

from sqlalchemy import Column, Float, String
from sqlalchemy.orm import relationship

from app.domain.hours import Hours
from app.infrastructure.database import Base
from app.usecase.hours import HoursReadModel


def unixtimestamp() -> int:
    return int(datetime.now().timestamp() * 1000)





class HoursDTO(Base):

    __tablename__ = "hours"
    id: Union[str, Column] = Column(String, primary_key=True, autoincrement=False)
    user_id: Union[str, Column] = Column(String, autoincrement=False)
    day: Union[str, Column] = Column(String, nullable=False, autoincrement=False)
    minutes:Union[float, Column] = Column(Float, nullable=False)

    def to_entity(self) -> Hours:
        return Hours(
            id=self.id,
            user_id=self.user_id,
            day=self.day,
            minutes=self.minutes,
        )

    def to_read_model(self) -> HoursReadModel:
        return HoursReadModel(
            id=self.id,
            user_id=self.user_id,
            day=self.day,
            minutes=self.minutes,
        )

    @staticmethod
    def from_entity(hours: Hours) -> "HoursDTO":
        now = unixtimestamp()
        if hours.created_at is None:
            hours.created_at = now
        return HoursDTO(
            id=hours.id,
            user_id=hours.user_id,
            day=hours.day,
            minutes=hours.minutes,
        )