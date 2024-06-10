from dataclasses import dataclass
from src.auth.auth import Auth

@dataclass
class User:
    user_id: str
    user_name: str
    _password: str
    _role: str

    def login(self):
        auth = Auth()

        auth.authenticate(self.user_id, self._password)