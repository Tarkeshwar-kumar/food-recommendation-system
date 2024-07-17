from dataclasses import dataclass
from abc import ABCMeta, abstractmethod
from server.db.db import DatabaseMethods
from server.model.food import Food
from server.validators.validation import food_exists_in_menu, is_valid_feedback, have_not_voted
from server.model.feedback import Feedback
from server.model.recommendation import Recommendation
from server.model.notification import AuditNotification

@dataclass
class User:
    user_id: str
    user_name: str
    role: str

    def login(self):
        db = DatabaseMethods()

        db.authenticate(self.user_id, self._password)

    def display_menu(self):
        db = DatabaseMethods()
        return db.display_menu()



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


    def change_food_price(self, food_id : str, new_price: float):
        db = DatabaseMethods()
        db.update_food_price(food_id, new_price)


    def change_food_availability(self, food_id : str):
        db = DatabaseMethods()
        db.update_food_availability(food_id)

    
    def remove_item_from_menu(self, food_id : str):
        db = DatabaseMethods()
        db.delete_item_from_menu(food_id)


class EmployeeService(metaclass = ABCMeta):
    @abstractmethod
    def give_feedback_on_food():
        pass

    @abstractmethod
    def vote_food_recommended():
        pass

    @abstractmethod
    def submit_improvement_feedback(self, user_id, json_data):
        pass


@dataclass
class Employee(User, EmployeeService):
    
    def give_feedback_on_food(self, feedback: Feedback):
        if is_valid_feedback(feedback.food_name, feedback.user_id):
            db = DatabaseMethods()
            db.insert_into_feedback(feedback)

    def vote_food_recommended(self, user_id: str, food_name: str):
        if have_not_voted(user_id, food_name):
            db = DatabaseMethods()
            db.vote_for_food_item(user_id, food_name)


    def get_food_recommendation(self, user_id, limit):
        recommendation = Recommendation()
        return recommendation.recommend_food(user_id, limit)
    
    def update_profile(self, user_id: str, json_data):
        db = DatabaseMethods()
        db.update_profile(user_id, json_data)

    def submit_improvement_feedback(self, user_id, json_data):
        db = DatabaseMethods()
        db.submit_food_audit_feedback(user_id, json_data)

class ChefService(metaclass = ABCMeta):
    @abstractmethod
    def rollout_food_recommendation():
        pass

    @abstractmethod
    def audit_food():
        pass

@dataclass
class Chef(User, ChefService):
    
    def rollout_food_recommendation(self, food_list):

        for food in food_list:
            if not food_exists_in_menu(food):
                raise ValueError("Food name is not valid")
        
        db = DatabaseMethods()
        db.delete_table()
        for food in food_list:
            db.insert_item_for_recommendation(food)

    def get_food_recommendation(self, limit):
        recommendation = Recommendation()
        return recommendation.recommend_food(limit)
    
    def audit_food(self, user: User, json_data):
        db = DatabaseMethods()
        food_list = db.get_food_list()

        for food in food_list:
            avg_rating = db.calculate_avg_rating(food)
            if avg_rating == None:
                avg_rating = 0
            print("rating" , avg_rating)
            if avg_rating < 2:
                db.add_food_to_discard_menu(food, avg_rating)
                print(food)
                notification = AuditNotification()
                return notification.send_notification(food)
            
    