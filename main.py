from user_validators import EmailValidator, UsernameFormatValidator
from user import UserService, User
from usernames_registry import UsernamesRegistry

usernames_registry = UsernamesRegistry()
username_format_validator = UsernameFormatValidator(usernames_registry)
email_validator = EmailValidator()
user_service = UserService(username_format_validator, email_validator)
my_1_user = User("anastasiia1", "anastasiia@example.com", user_service)
my_2_user = User("anastasiia1", "anastasiia@example.com", user_service)
