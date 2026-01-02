from .user import User, MembershipLevel, UserService


class RegularUser(User):
    def __init__(
        self,
        username: str,
        email: str,
        membership_level: MembershipLevel,
        user_service: UserService,
    ):
        super().__init__(username, email, user_service)
        self.membership_level = membership_level

    def get_info(self) -> str:
        return (
            super().get_info()
            + f" user`s membership level is {self.membership_level.value}"
        )
