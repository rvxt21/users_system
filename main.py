from users_system.exceptions import BaseUsersProgramException
from users_system.models.user import User
from users_system.models.admin import Admin
from users_system.models.usernames_registry import UsernamesRegistry

usernames_registry = UsernamesRegistry()

try:
    my_1_user = User("anastasiia1", "anastasiia@example.com")
    my_2_user = User("anastasiia1", "anastasiia@example.com")
    my_admin_user = Admin("admin1", "myadmin@example.com")
except BaseUsersProgramException as e:
    print(f"Error while creating user: {e}")
