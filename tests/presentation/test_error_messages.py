from app.presentation.schema.hours.hours_error_message import ErrorMessageHoursNotFound, \
    ErrorMessageHoursDayAlreadyExists, ErrorMessageHoursNotValidDate
from app.presentation.schema.resources.resources_error_message import ErrorMessageResourcesNotFound


class TestErrorMessages:
    def test_error_messages(self):
        assert ErrorMessageHoursNotFound is not ErrorMessageHoursDayAlreadyExists
        assert ErrorMessageHoursNotFound is not ErrorMessageHoursNotValidDate
        assert ErrorMessageHoursNotValidDate is not ErrorMessageHoursDayAlreadyExists
        assert ErrorMessageHoursNotFound is not ErrorMessageResourcesNotFound
