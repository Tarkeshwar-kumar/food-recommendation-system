from enum import Enum


class NotificationType(Enum):
    ADD_ITEM = 1
    REMOVE_ITEM = 2
    FOOD_AVAILABLE = 3
    FOOD_UNAVAILABLE = 4
