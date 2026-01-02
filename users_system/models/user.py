from users_system.validators.user_validators import (
    EmailValidator,
    UsernameFormatValidator,
)
from enum import Enum


class MembershipLevel(Enum):
    FREE = "free"
    PREMIUM = "premium"


class UserRoles(Enum):
    ADMIN = "admin"


class UserService:
    def __init__(
        self,
        username_validator: UsernameFormatValidator,
        email_validator: EmailValidator,
    ):
        self.username_validator = username_validator
        self.email_validator = email_validator


class User:
    def __init__(self, username: str, email: str, user_service: UserService):
        self.user_service = user_service
        self.user_service.username_validator.register_username(username)
        self.user_service.email_validator.validate_email(email)
        self.username = username
        self.email = email

    def get_info(self) -> str:
        return (
            f"User`s username is {self.username}, user`s email is {self.email}"
        )

    def login(self):
        return f"User {self.username} is logged in"
