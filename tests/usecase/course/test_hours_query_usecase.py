from unittest.mock import MagicMock, Mock

import pytest

from app.domain.hours import HoursNotFoundError
from app.infrastructure.hours import HoursQueryServiceImpl

from app.usecase.hours import HoursReadModel, HoursQueryUseCaseImpl


class TestHoursQueryUseCase:
    def test_fetch_course_by_id_should_return_course(self):

        session = MagicMock()
        course_query_service = HoursQueryServiceImpl(session)
        course_query_service.find_by_id = Mock(
            return_value= HoursReadModel(
                id="QK6qXDKUYf3p8x7Vb4SNas",
                user_id="106226",
                task_id="P03",
                day="2020-10-10",
                minutes=60,
                note="Un buen trabajo",
            )
        )

        course_query_usecase = HoursQueryUseCaseImpl(course_query_service)

        hours = course_query_usecase.fetch_hours_by_id("QK6qXDKUYf3p8x7Vb4SNas")

        assert hours.user_id == "106226"

    def test_fetch_course_by_id_should_throw_course_not_found_error(self):

        session = MagicMock()
        course_query_service = HoursQueryServiceImpl(session)
        course_query_service.find_by_id = Mock(side_effect=HoursNotFoundError)

        course_query_usecase = HoursQueryUseCaseImpl(course_query_service)

        with pytest.raises(HoursNotFoundError):
            course_query_usecase.fetch_hours_by_id("cPqw4yPVUM3fA9sqzpZmkL")

    def test_fetch_courses_should_return_courses(self):
        session = MagicMock()
        hours_query_service = HoursQueryServiceImpl(session)
        hours_query_service.find_all = Mock(
            return_value=[
                HoursReadModel(
                    id="QK6qXDKUYf3p8x7Vb4SNas",
                    user_id="106226",
                    task_id="P03",
                    day="2020-10-10",
                    minutes=70,
                    note="Un buen trabajo",
                ),
                HoursReadModel(
                    id="cPqw4yPVUM3fA9sqzpZmkL",
                    user_id="106000",
                    task_id="P03",
                    day="2020-10-10",
                    minutes=60,
                    note="Un buen trabajo",
                ),
            ]
        )

        course_query_usecase = HoursQueryUseCaseImpl(hours_query_service)
        courses = course_query_usecase.fetch_hours()

        assert len(courses) == 2
        assert courses[0].user_id == "106226"
        assert courses[0].minutes == 70
        assert courses[1].user_id == "106000"
        assert courses[1].minutes == 60

