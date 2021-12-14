from typing import Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app.domain.hours import Hours, HoursRepository
from app.usecase.hours import HoursCommandUseCaseUnitOfWork

from .hours_dto import HoursDTO


class HoursRepositoryImpl(HoursRepository):
    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: str) -> Optional[Hours]:
        try:
            hours_dto = self.session.query(HoursDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return hours_dto.to_entity()

    def create(self, hours: Hours):
        hours_dto = HoursDTO.from_entity(hours)
        try:
            self.session.add(hours_dto)
        except:
            raise

    def delete_by_id(self, id: str):
        try:
            hours = self.session.query(HoursDTO).filter_by(id=id).first()
            self.session.delete(hours)
        except:
            raise

    def find_existing_hours(self, day, user_id, task_id) -> Optional[Hours]:
        try:
            hours_dto = self.session.query(HoursDTO).filter_by(
                day=day,
                user_id=user_id,
                task_id=task_id
            ).one()
        except NoResultFound:
            return None
        except:
            raise

        return hours_dto.to_entity()


class HoursCommandUseCaseUnitOfWorkImpl(HoursCommandUseCaseUnitOfWork):
    def __init__(
        self,
        session: Session,
        hours_repository: HoursRepository,
    ):
        self.session: Session = session
        self.hours_repository: HoursRepository = hours_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
