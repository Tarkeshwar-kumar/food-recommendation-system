from dataclasses import dataclass, field
from server.utils.notification import NotificationType
from server.db.db import DatabaseMethods

@dataclass
class Notification:

    message: str = field(init=False, default=None)
    date: str = field(init=False, default=None)

    def send_notification(self):
        pass


class AddItemNotification(Notification):
    def send_notification(self, food_name: str):
        db = DatabaseMethods()
        user_id_list = db.get_epmloyee_list()
        for user_id in user_id_list:
            user_id = user_id[0]
            print("user id is ", user_id)
            db.insert_notification(user_id, NotificationType.ADD_ITEM.value, food_name)


class RemoveItemNotification(Notification):
    def send_notification(self, food_name: str):
        db = DatabaseMethods()
        user_id_list = db.get_epmloyee_list()
        for user_id in user_id_list:
            user_id = user_id[0]
            db.insert_notification(user_id, NotificationType.REMOVE_ITEM.value, food_name)

class FoodAvailabilityNotification(Notification):
    def send_notification(self, food_name: str):
        db = DatabaseMethods()
        user_id_list = db.get_epmloyee_list()
        for user_id in user_id_list:
            user_id = user_id[0]
            db.insert_notification(user_id, NotificationType.FOOD_AVAILABILITY_CHANGED.value, food_name)

class AuditNotification(Notification):
    def send_notification(self, food_name: str):
        db = DatabaseMethods()
        user_id_list = db.get_epmloyee_list()
        for user_id in user_id_list:
            user_id = user_id[0]
            db.insert_notification(user_id, NotificationType.FOOD_AUDIT.value, food_name)