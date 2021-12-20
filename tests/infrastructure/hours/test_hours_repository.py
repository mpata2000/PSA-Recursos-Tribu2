from unittest.mock import MagicMock, Mock

import pytest
from sqlalchemy.exc import NoResultFound

from app.domain.hours import HoursNotFoundError, Hours, HoursDayAlreadyExistsError
from app.infrastructure.hours import HoursDTO, HoursRepositoryImpl

hours_1 = Hours(
    id="QK6qXDKUYf3p8x7Vb4SNas",
    user_id="106226",
    task_id="P03",
    day="2020-10-10",
    hours=3,
    minutes=34,
    seconds=24,
    note="Un buen trabajo",
)

hours_dto_1 = HoursDTO(
    id="QK6qXDKUYf3p8x7Vb4SNas",
    user_id="106226",
    task_id="P03",
    day="2020-10-10",
    hours=3,
    minutes=34,
    seconds=24,
    note="Un buen trabajo",
)

query_hours = MagicMock()
query_hours.one = Mock(return_value=hours_dto_1)
query_hours.first = Mock(return_value=hours_dto_1)


def mock_filter_hours(id):
    if id == hours_dto_1.id:
        return query_hours
    raise HoursNotFoundError


class TestHoursRepository:
    def test_find_by_id_should_return_hours(self):
        session = MagicMock()
        session.query(HoursDTO).filter_by = Mock(side_effect=mock_filter_hours)
        hours_repository = HoursRepositoryImpl(session)

        hour = hours_repository.find_by_id("QK6qXDKUYf3p8x7Vb4SNas")

        session.query(HoursDTO).filter_by.assert_called_with(id="QK6qXDKUYf3p8x7Vb4SNas")
        assert hour.user_id == "106226"

    def test_find_by_id_should_throw_hours_not_found_error(self):
        session = MagicMock()
        session.query(HoursDTO).filter_by = Mock(side_effect=HoursNotFoundError)
        hours_repository = HoursRepositoryImpl(session)

        with pytest.raises(HoursNotFoundError):
            hours_repository.find_by_id("cPqw4yPVUM3fA9sqzpZmkL")
        session.query(HoursDTO).filter_by.assert_called_with(
            id="cPqw4yPVUM3fA9sqzpZmkL"
        )

    def test_find_by_id_should_throw_no_result_found(self):
        session = MagicMock()
        session.query(HoursDTO).filter_by = Mock(side_effect=NoResultFound)
        course_repository = HoursRepositoryImpl(session)

        courses = course_repository.find_by_id("cPqw4yPVUM3fA9sqzpZmkL")

        assert courses is None
        session.query(HoursDTO).filter_by.assert_called_with(
            id="cPqw4yPVUM3fA9sqzpZmkL"
        )

    def test_create_should_add_course_dto(self):
        session = MagicMock()
        session.add = Mock()
        course_repository = HoursRepositoryImpl(session)

        course_repository.create(
            Hours(
                id="QK6qXDKUYf3p8x7Vb4SNas",
                user_id="106226",
                task_id="P03",
                day="2020-10-10",
                hours=3,
                minutes=34,
                seconds=24,
                note="Un buen trabajo",
            )
        )

        session.add.assert_called_once()

    def test_create_should_throw_hour_already_exists_error(self):
        session = MagicMock()
        session.add = Mock(side_effect=HoursDayAlreadyExistsError)
        course_repository = HoursRepositoryImpl(session)

        with pytest.raises(HoursDayAlreadyExistsError):
            course_repository.create(
                Hours(
                    id="QK6qXDKUYf3p8x7Vb4SNas",
                    user_id="106226",
                    task_id="P03",
                    day="2020-10-10",
                    hours=3,
                    minutes=34,
                    seconds=24,
                    note="Un buen trabajo",
                )
            )
        session.add.assert_called_once()

    def test_existing_hours_should_find_existing_hours(self):
        session = MagicMock()
        session.query(HoursDTO).filter_by = Mock(side_effect=query_hours)
        hours_repository = HoursRepositoryImpl(session)

        hours = hours_repository.find_existing_hours(day="2020-10-10", user_id="106226", task_id="P03")
        # assert hours == hours_1
        session.query(HoursDTO).filter_by.assert_called_with(day="2020-10-10", user_id="106226", task_id="P03")

    def test_existing_hours_of_non_existing_hours_retuns_none(self):
        session = MagicMock()
        session.query(HoursDTO).filter_by = Mock(side_effect=NoResultFound)
        hours_repository = HoursRepositoryImpl(session)

        hours = hours_repository.find_existing_hours(day="2020-10-10", user_id="106226", task_id="P03")
        session.query(HoursDTO).filter_by.assert_called_with(day="2020-10-10", user_id="106226", task_id="P03")
        assert hours is None

    def test_existing_hours_should_rais_unspecified_exception(self):
        session = MagicMock()
        session.query(HoursDTO).filter_by = Mock(side_effect=HoursNotFoundError)
        hours_repository = HoursRepositoryImpl(session)

        with pytest.raises(HoursNotFoundError):
            hours_repository.find_existing_hours(day="2020-10-10", user_id="106226", task_id="P03")


    def test_delete_by_id_should_delete_correct_course(self):
        session = MagicMock()
        session.query(HoursDTO).filter_by = Mock(side_effect=query_hours)
        course_repository = HoursRepositoryImpl(session)

        course_repository.delete_by_id(id="QK6qXDKUYf3p8x7Vb4SNas")

        session.query(HoursDTO).filter_by.assert_called_with(id="QK6qXDKUYf3p8x7Vb4SNas")

    def test_delete_by_id_should_throw_course_not_found_error(self):
        session = MagicMock()
        session.query(HoursDTO).filter_by = Mock(side_effect=HoursNotFoundError)
        course_repository = HoursRepositoryImpl(session)

        with pytest.raises(HoursNotFoundError):
            course_repository.delete_by_id(id="h_1")
        session.query(HoursDTO).filter_by.assert_called_with(id="h_1")
