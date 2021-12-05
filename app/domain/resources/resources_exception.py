
class ResourcesNotFoundError(Exception):
    message = "No Resources were found."

    def __str__(self):
        return ResourcesNotFoundError.message
