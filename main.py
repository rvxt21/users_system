from user_validators import EmailValidator, UsernameFormatValidator
from exceptions import BaseUsersProgramException
from user import UserService, User, Admin
from usernames_registry import UsernamesRegistry

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
