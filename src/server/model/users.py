from dataclasses import dataclass
from abc import ABCMeta, abstractmethod
from server.db.db import DatabaseMethods
from server.model.food import Food, Feedback
from server.validators.validation import is_valid_food

@dataclass
class User:
    user_id: str
    user_name: str
    role: str

    def login(self):
        db = DatabaseMethods()

        db.authenticate(self.user_id, self._password)

    def display_menu():
        pass


class AdminService(metaclass = ABCMeta):
    @abstractmethod
    def add_item_to_menu(self, food: Food):
        pass

    @abstractmethod
    def change_food_price(self, new_price):
        pass


    @abstractmethod
    def change_food_availability(food_id : str, avilability: bool):
        pass

    @abstractmethod
    def remove_item_from_menu(food_id : str):
        pass


@dataclass
class Admin(User, AdminService):
    def add_item_to_menu(self, food : Food):
        db = DatabaseMethods()
        db.insert_item_to_menu(food)


    def change_food_price(food_id : str, new_price: float):
        db = DatabaseMethods()
        db.update_food_price(food_id, new_price)


    def change_food_availability(food_id : str, avilability: bool):
        db = DatabaseMethods()
        db.update_food_availability(food_id, avilability)

    
    def remove_item_from_menu(food_id : str):
        db = DatabaseMethods()
        db.delete_item_from_menu(food_id)


@dataclass
class Employee(User):
    
    def give_feedback_on_food():
        pass

    def vote_food_remmended():
        pass

class AdminService(metaclass = ABCMeta):
    @abstractmethod
    def rollout_food_recommendation():
        pass

@dataclass
class Chef(User, AdminService):
    
    def rollout_food_recommendation(self, food_list):
        for food in food_list:
            if not is_valid_food(food):
                raise ValueError("Food name is not valid")
            
        for food in food_list:
            db = DatabaseMethods()
            db.insert_item_for_recommendation(food)
