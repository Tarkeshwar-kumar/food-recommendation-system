import mysql.connector as sql
from server.validators.validation import is_valid_user

class Auth:
    def authenticate(self, user_id: str, password: str):
        if is_valid_user(user_id, password):
            return True
        return False