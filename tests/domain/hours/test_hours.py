from datetime import datetime

import pytest

from app.domain.hours import Hours


class TestHours:
    def test_constructor_should_create_instance(self):
        hours = Hours(
            id="QK6qXDKUYf3p8x7Vb4SNas",
            user_id="106226",
            task_id="P03",
            day="2020-10-10",
            minutes=60,
            note="Un buen trabajo",
        )

        assert hours.id == "QK6qXDKUYf3p8x7Vb4SNas"
        assert hours.user_id == "106226"
        assert hours.task_id == "P03"
        assert hours.day == "2020-10-10"
        assert hours.minutes == 60
        assert hours.note == "Un buen trabajo"

    def test_course_entity_should_be_identified_by_id(self):
        hours_1 = Hours(
            id="1",
            user_id="106226",
            task_id="P03",
            day="2020-10-10",
            minutes=60,
            note="Un buen trabajo",
        )

        hours_2 = Hours(
            id="1",
            user_id="106226",
            task_id="P03",
            day="2020-10-10",
            minutes=60,
            note="Un buen trabajo",
        )

        hours_3 = Hours(
            id="3",
            user_id="106226",
            task_id="P03",
            day="2020-10-10",
            minutes=60,
            note="Un buen trabajo",
        )

        assert hours_1 == hours_2
        assert hours_1 != hours_3


    def test_constructor_note_should_be_optional(self):
        hours = Hours(
            id="QK6qXDKUYf3p8x7Vb4SNas",
            user_id="106226",
            task_id="P03",
            day="2020-10-10",
            minutes=60,
        )

        assert hours.id == "QK6qXDKUYf3p8x7Vb4SNas"
        assert hours.user_id == "106226"
        assert hours.task_id == "P03"
        assert hours.day == "2020-10-10"
        assert hours.minutes == 60
        assert hours.note == None

'''    @pytest.mark.parametrize(
        "price",
        [
            (0),
            (1),
            (320),
        ],
    )
    def test_price_setter_should_update_value(self, price):
        hours = Course(
            id="course_01",
            name="C Programming For Beginners - Master the C Language",
            categories="Programming",
            price=10,
        )

        hours.price = price

        assert hours.price == price
'''
