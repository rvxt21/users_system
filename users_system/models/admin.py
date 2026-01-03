from .user import User, UserRoles


class Admin(User):
    def __init__(self, username: str, email: str):
        super().__init__(username, email)
        self.role = UserRoles.ADMIN

    def delete_user(self):
        return f"Admin {self.username} deleted user."

    def get_info(self):
        return super().get_info() + f" user is {self.role.value}"
