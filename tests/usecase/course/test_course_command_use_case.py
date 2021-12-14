
from unittest.mock import MagicMock, Mock

import pytest

from app.domain.hours import HoursNotFoundError, Hours, HoursDayAlreadyExistsError
from app.infrastructure.hours import HoursDTO, HoursCommandUseCaseUnitOfWorkImpl, HoursRepositoryImpl
from app.usecase.hours import HoursCommandUseCaseImpl

hours_1 = Hours(
    id="QK6qXDKUYf3p8x7Vb4SNas",
    user_id="106226",
    task_id="P03",
    day="2020-10-10",
    minutes=60,
    note="Un buen trabajo",
)

hours_dto_1= HoursDTO(
    id="QK6qXDKUYf3p8x7Vb4SNas",
    user_id="106226",
    task_id="P03",
    day="2020-10-10",
    minutes=60,
    note="Un buen trabajo",
)

query_course_1 = MagicMock()
query_course_1.one = Mock(return_value=hours_dto_1)
query_course_1.first = Mock(return_value=hours_dto_1)

def mock_filter_hours_1(id):
    if id == hours_dto_1.id:
        return query_course_1
    raise HoursNotFoundError


class TestCourseCommandUseCase:
    '''    def test_create_course_should_return_course(self):
        session = MagicMock()
        hours_repository = MagicMock()
        hours_repository.find_existing_hours = Mock(return_value=None)

        uow = HoursCommandUseCaseUnitOfWorkImpl(
            session=session, hours_repository=hours_repository
        )
        hours_command_usecase = HoursCommandUseCaseImpl(uow=uow)

        hours = hours_command_usecase.create_hours(hours_1)

        assert hours.user_id == hours.user_id
        hours_repository.find_existing_hours.assert_called_with(hours_1.day, hours_1.user_id, hours_1.task_id)'''

    def test_create_course_when_course_exists_should_throw_course_name_already_exists_error(
        self,
    ):
        session = MagicMock()
        hours_repository = MagicMock()
        hours_repository.find_by_name = Mock(
            side_effect=mock_filter_hours_1
        )
        hours_repository.find_existing_hours = Mock(return_value=hours_1)
        uow = HoursCommandUseCaseUnitOfWorkImpl(
            session=session, hours_repository=hours_repository
        )
        course_command_usecase = HoursCommandUseCaseImpl(uow=uow)

        with pytest.raises(HoursDayAlreadyExistsError):
            course_command_usecase.create_hours(hours_1)
        hours_repository.find_existing_hours.assert_called_with(hours_1.day, hours_1.user_id, hours_1.task_id)

    '''def test_update_course_should_return_course(self):
        session = MagicMock()
        course_repository = MagicMock()
        course_repository.find_by_id = Mock(return_value=course_1)
        uow = CourseCommandUseCaseUnitOfWorkImpl(
            session=session, course_repository=course_repository
        )
        course_command_usecase = CourseCommandUseCaseImpl(uow=uow)

        course = course_command_usecase.update_course(
            id=course_1.id, data=course_1_update
        )

        assert course.name == course_1.name'''

    def test_delete_course_by_id(self):
        session = MagicMock()
        session.query(HoursDTO).filter_by = Mock(side_effect=mock_filter_hours_1)
        hours_repository = HoursRepositoryImpl(session)
        uow = HoursCommandUseCaseUnitOfWorkImpl(
            session=session, hours_repository=hours_repository
        )
        course_command_usecase = HoursCommandUseCaseImpl(uow=uow)

        course_command_usecase.delete_hours_by_id(id=hours_1.id)

        session.query(HoursDTO).filter_by.assert_called_with(id="QK6qXDKUYf3p8x7Vb4SNas")


