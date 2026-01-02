import re

from exceptions import (
    UsernameAlreadyExistsError,
    InvalidEmailError,
    InvalidUsernameFormatError,
)
from usernames_registry import UsernamesRegistry


class EmailValidator:
    @staticmethod
    def validate_email(email: str):
        email_validation_pattern: str = r"^\S+@\S+\.\S+$"
        if not re.fullmatch(email_validation_pattern, email):
            raise InvalidEmailError(f"Invalid email: {email}")


class UsernameFormatValidator:
    def __init__(self, taken_usernames: UsernamesRegistry):
        self.taken_usernames = taken_usernames

    def register_username(self, username: str):
        self._validate_correct_username_format(username)
        if username.lower() in self.taken_usernames.usernames:
            raise UsernameAlreadyExistsError("Username should be unique")

        self.taken_usernames.usernames.add(username.lower())

    @staticmethod
    def _validate_correct_username_format(username: str):
        username_validation_pattern: str = (
            "^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$"
        )
        if not re.fullmatch(username_validation_pattern, username):
            raise InvalidUsernameFormatError(
                f"Invalid username format: {username}"
            )
