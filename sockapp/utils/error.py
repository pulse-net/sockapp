from sockx.utils.error import CustomException


class InvalidStartingDirectory(CustomException):
    def __init__(self, message):
        super().__init__(message=message)