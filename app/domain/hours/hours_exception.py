class HoursNotFoundError(Exception):
    message = "The Hours for the day you specified do not exist."

    def __str__(self):
        return HoursNotFoundError.message


class HoursDayAlreadyExistsError(Exception):
    message = "Hours for the day you specified already exist."

    def __str__(self):
        return HoursDayAlreadyExistsError.message


class HoursNotFoundError(Exception):
    message = "No Hours were found."

    def __str__(self):
        return HoursNotFoundError.message

class HoursNotValidDateError(Exception):
    message = "invalid date format"

    def __str__(self):
        return HoursNotValidDateError.message
