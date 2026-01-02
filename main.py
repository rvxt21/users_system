from users_system.validators.user_validators import (
    EmailValidator,
    UsernameFormatValidator,
)
from users_system.exceptions.exceptions import BaseUsersProgramException
from users_system.models.user import UserService, User
from users_system.models.admin import Admin
from users_system.models.usernames_registry import UsernamesRegistry

usernames_registry = UsernamesRegistry()
username_format_validator = UsernameFormatValidator(usernames_registry)
email_validator = EmailValidator()
user_service = UserService(username_format_validator, email_validator)

try:
    my_1_user = User("anastasiia1", "anastasiia@example.com", user_service)
    my_2_user = User("anastasiia", "anastasiia@example.com", user_service)
    my_admin_user = Admin("admin1", "myadmin@example.com", user_service)
except BaseUsersProgramException as e:
    print(f"Error while creating user: {e}")
