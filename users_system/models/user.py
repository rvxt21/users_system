from users_system.validators.user_validators import (
    EmailValidator,
    UsernameFormatValidator,
)
from .usernames_registry import UsernamesRegistry
from enum import Enum


class MembershipLevel(Enum):
    FREE = "free"
    PREMIUM = "premium"


class UserRoles(Enum):
    ADMIN = "admin"


class User:
    def __init__(self, username: str, email: str):
        self.email_validator = EmailValidator(email)
        self.username_validator = UsernameFormatValidator(username)
        self.username_validator.validate()
        self.email_validator.validate()
        UsernamesRegistry().register_username(username)
        self.username = username
        self.email = email

    def get_info(self) -> str:
        return (
            f"User`s username is {self.username}, user`s email is {self.email}"
        )

    def login(self):
        return f"User {self.username} is logged in"
