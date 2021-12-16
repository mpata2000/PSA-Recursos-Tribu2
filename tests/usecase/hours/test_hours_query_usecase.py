from unittest.mock import MagicMock, Mock

import pytest

from app.domain.hours import HoursNotFoundError
from app.infrastructure.hours import HoursQueryServiceImpl

from app.usecase.hours import HoursReadModel, HoursQueryUseCaseImpl

hours_read_1 = HoursReadModel(
    id="1",
    user_id="106226",
    task_id="P03",
    day="2020-10-10",
    hours=2,
    minutes=35,
    seconds=10,
    note="Un buen trabajo",
)

hours_read_2 = HoursReadModel(
    id="2",
    user_id="106000",
    task_id="P03",
    day="2020-10-10",
    hours=2,
    minutes=40,
    seconds=10,
    note="Un buen trabajo",
)

hours_read_3 = HoursReadModel(
    id="3",
    user_id="106226",
    task_id="P04",
    day="2020-12-12",
    hours=2,
    minutes=50,
    seconds=10,
    note="Un buen trabajo",
)

class TestHoursQueryUseCase:
    def test_fetch_hours_by_id_should_return_hours(self):

        session = MagicMock()
        hours_query_service = HoursQueryServiceImpl(session)
        hours_query_service.find_by_id = Mock(
            return_value=hours_read_1
        )

        course_query_usecase = HoursQueryUseCaseImpl(hours_query_service)

        hours = course_query_usecase.fetch_hours_by_id("1")
        assert hours.user_id == "106226"
        hours_query_service.find_by_id.assert_called_with("1")

    def test_fetch_hours_by_id_should_throw_course_not_found_error(self):

        session = MagicMock()
        hours_query_service = HoursQueryServiceImpl(session)
        hours_query_service.find_by_id = Mock(side_effect=HoursNotFoundError)

        hours_query_usecase = HoursQueryUseCaseImpl(hours_query_service)

        with pytest.raises(HoursNotFoundError):
            hours_query_usecase.fetch_hours_by_id("2")
        hours_query_service.find_by_id.assert_called_with("2")

    def test_fetch_all_hours_should_return_hours(self):
        session = MagicMock()
        hours_query_service = HoursQueryServiceImpl(session)
        hours_query_service.find_all = Mock(
            return_value=[
                hours_read_1,
                hours_read_2,
            ]
        )

        hours_query_usecase = HoursQueryUseCaseImpl(hours_query_service)
        courses = hours_query_usecase.fetch_hours()

        assert len(courses) == 2
        assert courses[0].user_id == "106226"
        assert courses[0].minutes == 35
        assert courses[1].user_id == "106000"
        assert courses[1].minutes == 40

    def test_find_by_filter_hours_with_no_filter_should_return_hours(self):
        session = MagicMock()
        hours_query_service = HoursQueryServiceImpl(session)
        hours_query_service.find_by_filters = Mock(
            return_value=[
                hours_read_1,
                hours_read_2,
            ]
        )

        hours_query_usecase = HoursQueryUseCaseImpl(hours_query_service)
        courses = hours_query_usecase.fetch_hours_by_filters(
            ids=None,
            day=None,
            user_id=None,
            task_id=None,
        )

        hours_query_service.find_by_filters.assert_called_with(
            ids=None,
            day=None,
            user_id=None,
            task_id=None,
            limit=100,
            offset=0
        )
        assert len(courses) == 2
        assert courses[0].user_id == "106226"
        assert courses[0].minutes == 35
        assert courses[1].user_id == "106000"
        assert courses[1].minutes == 40

    def test_find_by_filter_hours_filter_by_user_id_should_return_hours(self):
        session = MagicMock()
        hours_query_service = HoursQueryServiceImpl(session)
        hours_query_service.find_by_filters = Mock(
            return_value=[
                hours_read_1,
                hours_read_3,
            ]
        )

        hours_query_usecase = HoursQueryUseCaseImpl(hours_query_service)
        courses = hours_query_usecase.fetch_hours_by_filters(
            ids=None,
            day=None,
            user_id="106226",
            task_id=None,
        )

        hours_query_service.find_by_filters.assert_called_with(
            ids=None,
            day=None,
            user_id="106226",
            task_id=None,
            limit=100,
            offset=0
        )
        assert len(courses) == 2
        assert courses[0].user_id == "106226"
        assert courses[0].minutes == 35
        assert courses[1].user_id == "106226"
        assert courses[1].minutes == 50

    def test_find_by_filter_hours_filter_by_task_id_should_return_hours(self):
        session = MagicMock()
        hours_query_service = HoursQueryServiceImpl(session)
        hours_query_service.find_by_filters = Mock(
            return_value=[
                hours_read_1,
                hours_read_2,
            ]
        )

        hours_query_usecase = HoursQueryUseCaseImpl(hours_query_service)
        hours = hours_query_usecase.fetch_hours_by_filters(
            ids=None,
            day=None,
            user_id=None,
            task_id="P03",
        )

        hours_query_service.find_by_filters.assert_called_with(
            ids=None,
            day=None,
            user_id=None,
            task_id="P03",
            limit=100,
            offset=0
        )

        assert len(hours) == 2
        assert hours[0].user_id == "106226"
        assert hours[0].task_id == "P03"
        assert hours[0].minutes == 35
        assert hours[1].user_id == "106000"
        assert hours[1].task_id == "P03"
        assert hours[1].minutes == 40

    def test_find_by_filter_hours_filter_by_day_should_return_hours(self):
        session = MagicMock()
        hours_query_service = HoursQueryServiceImpl(session)
        hours_query_service.find_by_filters = Mock(
            return_value=[
                hours_read_1,
                hours_read_2,
            ]
        )

        hours_query_usecase = HoursQueryUseCaseImpl(hours_query_service)
        hours = hours_query_usecase.fetch_hours_by_filters(
            ids=None,
            day="2020-10-10",
            user_id=None,
            task_id=None,
        )

        hours_query_service.find_by_filters.assert_called_with(
            ids=None,
            day="2020-10-10",
            user_id=None,
            task_id=None,
            limit=100,
            offset=0
        )

        assert len(hours) == 2
        assert hours[0].user_id == "106226"
        assert hours[0].task_id == "P03"
        assert hours[0].minutes == 35
        assert hours[1].user_id == "106000"
        assert hours[1].task_id == "P03"
        assert hours[1].minutes == 40

    def test_find_by_filter_hours_with_all_filters_should_return_hours(self):
        session = MagicMock()
        hours_query_service = HoursQueryServiceImpl(session)
        hours_query_service.find_by_filters = Mock(
            return_value=([hours_read_3], 1)
        )

        hours_query_usecase = HoursQueryUseCaseImpl(hours_query_service)
        hours, count = hours_query_usecase.fetch_hours_by_filters(
            ids="3",
            user_id="106226",
            task_id="P04",
            day="2020-12-12",
        )

        hours_query_service.find_by_filters.assert_called_with(
            ids="3",
            user_id="106226",
            task_id="P04",
            day="2020-12-12",
            limit=100,
            offset=0
        )

        assert len(hours) == 1
        assert count == 1
        assert hours[0].user_id == "106226"
        assert hours[0].task_id == "P04"
        assert hours[0].minutes == 50
