from .user import User, MembershipLevel


class RegularUser(User):
    def __init__(
        self,
        username: str,
        email: str,
        membership_level: MembershipLevel,
    ):
        super().__init__(
            username,
            email,
        )
        self.membership_level = membership_level

    def get_info(self) -> str:
        return (
            super().get_info()
            + f" user`s membership level is {self.membership_level.value}"
        )
