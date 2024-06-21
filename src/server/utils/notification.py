from enum import Enum


class NotificationType(Enum):
    ADD_ITEM = 1
    REMOVE_ITEM = 2
    FOOD_AVAILABILITY_CHANGED = 3
    FOOD_AUDIT = 4
