from server.db.db import DatabaseMethods

def is_valid_user(user_id: str, password: str) -> bool:
    return True


def food_exists_in_menu(food) -> bool:
    db = DatabaseMethods()
    if db.food_exists_in_menu(food):
        return True
    return False

def is_valid_feedback(food_name: str, user_id: str):
    db = DatabaseMethods()
    if db.is_valid_feedback(food_name, user_id):
        return True
    return False

def have_not_voted(user_id, food_name):
    db = DatabaseMethods()
    if db.have_not_voted(user_id, food_name):
        return True
    return False