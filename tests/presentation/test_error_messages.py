from app.presentation.schema.hours.hours_error_message import ErrorMessageHoursNotFound, \
    ErrorMessageHoursDayAlreadyExists, ErrorMessageHoursNotFoundInDate, ErrorMessageHoursNotValidDate
from app.presentation.schema.resources.resources_error_message import ErrorMessageResourcesNotFound


class TestErrorMessages:
    def test_error_messages(self):
        assert ErrorMessageHoursNotFound is not ErrorMessageHoursDayAlreadyExists
        assert ErrorMessageHoursNotFound is not ErrorMessageHoursNotFoundInDate
        assert ErrorMessageHoursNotFound is not ErrorMessageHoursNotValidDate
        assert ErrorMessageHoursNotValidDate is not ErrorMessageHoursDayAlreadyExists
        assert ErrorMessageHoursNotValidDate is not ErrorMessageHoursNotFoundInDate
        assert ErrorMessageHoursNotFound is not ErrorMessageResourcesNotFound
