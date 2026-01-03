class UsernamesRegistry:
    _instance = None
    usernames: set = set()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def register_username(self, username):
        self.usernames.add(username)
