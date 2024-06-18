from dataclasses import dataclass
from server.utils.notification import NotificationType
from server.db.db import DatabaseMethods
@dataclass
class Notification:

    message: str
    date: str

    def send_notification(self):
        pass


class AddItemNotification:
    def send_notification(self, food_name: str):
        db = DatabaseMethods()
        user_id_list = db.get_epmloyee_list()
        for user_id in user_id_list:
            user_id = user_id[0]
            print("user id is ", user_id)
            db.insert_notification(user_id, NotificationType.ADD_ITEM.value, food_name)


class RemoveItemNotification:
    def send_notification(self, food_name: str):
        db = DatabaseMethods()
        user_id_list = db.get_epmloyee_list()
        for user_id in user_id_list:
            user_id = user_id[0]
            db.insert_notification(user_id, NotificationType.REMOVE_ITEM.value, food_name)

class FoodUnavailableNotification:
    def send_notification(self, food_name: str):
        db = DatabaseMethods()
        user_id_list = db.get_epmloyee_list()
        for user_id in user_id_list:
            user_id = user_id[0]
            db.insert_notification(user_id, NotificationType.FOOD_UNAVAILABLE.value, food_name)

class FoodAvailableNotification:
    def send_notification(self, food_name: str):
        db = DatabaseMethods()
        user_id_list = db.get_epmloyee_list()
        for user_id in user_id_list:
            user_id = user_id[0]
            db.insert_notification(user_id, NotificationType.FOOD_AVAILABLE.value, food_name)