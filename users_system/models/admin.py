from .user import User, UserService, UserRoles


class Admin(User):
    def __init__(self, username: str, email: str, user_service: UserService):
        super().__init__(username, email, user_service)
        self.role = UserRoles.ADMIN

    def delete_user(self):
        return f"Admin {self.username} deleted user."

    def get_info(self):
        return super().get_info() + f" user is {self.role.value}"
