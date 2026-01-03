import re

from users_system.exceptions import (
    InvalidEmailError,
    InvalidUsernameFormatError,
    UsernameAlreadyExistsError,
)
from users_system.models.usernames_registry import UsernamesRegistry

from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self) -> None:
        pass


class EmailValidator(Validator):
    def __init__(self, email: str):
        self.email = email

    def validate(self):
        email_validation_pattern: str = r"^\S+@\S+\.\S+$"
        if not re.fullmatch(email_validation_pattern, self.email):
            raise InvalidEmailError(f"Invalid email: {self.email}")


class UsernameFormatValidator(Validator):
    def __init__(self, username: str):
        self.username_registry = UsernamesRegistry()
        self.username = username

    def validate(self):
        username_validation_pattern: str = (
            r"^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$"
        )
        if self.username in self.username_registry.usernames:
            raise UsernameAlreadyExistsError("Username should be unique")

        elif not re.fullmatch(username_validation_pattern, self.username):
            raise InvalidUsernameFormatError(
                f"Invalid username format: {self.username}"
            )
