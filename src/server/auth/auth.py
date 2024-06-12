import mysql.connector as sql


class Auth:
    def authenticate(user_id: str, password: str):
        if user_id == "user_id" and password == "password":
            return True
        return False