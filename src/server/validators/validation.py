from server.db.db import DatabaseMethods

def is_valid_user(user_id: str, password: str) -> bool:
    return True


def is_valid_food(food) -> bool:
    db = DatabaseMethods()
    if db.food_exists_in_menu(food):
        return True
    return False