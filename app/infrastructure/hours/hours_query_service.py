from datetime import date
from typing import List, Optional, Tuple

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app.usecase.hours import HoursQueryService, HoursReadModel

from ...domain.hours import HoursNotFoundError
from .hours_dto import HoursDTO


class HoursQueryServiceImpl(HoursQueryService):
    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: str) -> Optional[HoursReadModel]:
        try:
            hours_dto = self.session.query(HoursDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return hours_dto.to_read_model()

    def find_all(
            self, limit: int = 100, offset: int = 0
    ) -> Tuple[List[HoursReadModel], int]:
        try:
            hours_dtos = (
                self.session.query(HoursDTO)
                    .slice(limit * offset, limit * (offset + 1))
                    .all()
            )
        except:
            raise HoursNotFoundError

        return (
            list(map(lambda hours_dto: hours_dto.to_read_model(), hours_dtos)),
            self.session.query(HoursDTO).count(),
        )

    def find_by_filters(
            self,
            ids: Optional[List[str]],
            day: Optional[date],
            user_id: Optional[str],
            task_id: Optional[str],
            limit: int = 100,
            offset: int = 0,
    ) -> Tuple[List[HoursReadModel], int]:
        try:
            hours_q = self.session.query(HoursDTO)

            if ids:
                hours_q = hours_q.filter(HoursDTO.id.in_(ids))  # type: ignore
            if day:
                hours_q = hours_q.filter_by(day=day)
            if user_id:
                hours_q = hours_q.filter_by(user_id=user_id)
            if task_id:
                hours_q = hours_q.filter_by(task_id=task_id)

            hours_dtos = hours_q.slice(limit * offset, limit * (offset + 1)).all()
        except:
            raise

        return (
            list(map(lambda hours_dto: hours_dto.to_read_model(), hours_dtos)),
            hours_q.count(),
        )
#Fix lint error
