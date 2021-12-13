from datetime import datetime

from app.domain.hours import Hours
from app.infrastructure.hours import HoursDTO


class TestHoursDTO:
    def test_to_read_model_should_create_entity_instance(self):
        hours_dto = HoursDTO(
            id="QK6qXDKUYf3p8x7Vb4SNas",
            user_id="106226",
            task_id="P03",
            day="2020-10-10",
            minutes=60,
            note="Un buen trabajo",
        )

        hours = hours_dto.to_read_model()

        assert hours.id == "QK6qXDKUYf3p8x7Vb4SNas"
        assert hours.user_id == "106226"
        assert hours.task_id == "P03"
        assert hours.day.strftime("%Y-%m-%d") == "2020-10-10"
        assert hours.minutes == 60
        assert hours.note == "Un buen trabajo"

    def test_to_entity_should_create_entity_instance(self):
        hours_dto = HoursDTO(
            id="QK6qXDKUYf3p8x7Vb4SNas",
            user_id="106226",
            task_id="P03",
            day="2020-10-10",
            minutes=60,
            note="Un buen trabajo",
        )

        hours = hours_dto.to_entity()

        assert hours.id == "QK6qXDKUYf3p8x7Vb4SNas"
        assert hours.user_id == "106226"
        assert hours.task_id == "P03"
        assert hours.day == "2020-10-10"
        assert hours.minutes == 60
        assert hours.note == "Un buen trabajo"

    def test_from_entity_should_create_dto_instance(self):
        hours = Hours(
            id="QK6qXDKUYf3p8x7Vb4SNas",
            user_id="106226",
            task_id="P03",
            day="2020-10-10",
            minutes=60,
            note="Un buen trabajo",
        )

        hours_dto = HoursDTO.from_entity(hours)

        assert hours_dto.id == "QK6qXDKUYf3p8x7Vb4SNas"
        assert hours_dto.user_id == "106226"
        assert hours_dto.task_id == "P03"
        assert hours_dto.day == "2020-10-10"
        assert hours_dto.minutes == 60
        assert hours_dto.note == "Un buen trabajo"
