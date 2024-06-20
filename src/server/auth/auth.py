from server.db.db import DatabaseMethods

class Auth:
    def login():
        pass

    def logout(self, user_id, attempt_type):
        db = DatabaseMethods()
        return db.log_login_attempts(user_id, True, attempt_type)


    def log_login_attempts(self, user_id, is_logged_in):
        db = DatabaseMethods()
        db.log_login_attempts(user_id, is_logged_in, "Login")
