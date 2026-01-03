class BaseUsersProgramException(Exception):
    pass


class UsernameAlreadyExistsError(BaseUsersProgramException):
    pass


class InvalidEmailError(BaseUsersProgramException):
    pass


class InvalidUsernameFormatError(BaseUsersProgramException):
    pass
