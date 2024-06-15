from server.model.users import Admin, Chef, Employee, User
from server.db.db import DatabaseMethods
class UserFactory:
    @staticmethod
    def create_user(user_id):
        db = DatabaseMethods()
        user_id, user_name, role = db.get_user_details(user_id)
        if role == "Admin":
            return Admin(user_id, user_name, role)
        elif role == "Chef":
            return Chef(user_id, user_name, role)
        elif role == "Employee":
            return Employee(user_id, user_name, role)
        else:
            raise ValueError(f"Unknown role: {role}")
