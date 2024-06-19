from server.model.users import User
from server.db.db import DatabaseMethods
from server.model.food import Food
from server.model.feedback import Feedback
from server.utils.sentiment import RuleBasedSentiment
from server.model.notification import AddItemNotification, RemoveItemNotification
from server.exception.exceptions import FoodDoesNotExist
from server.utils.handler import *


def handle_display_menu(user: User, json_data):
    return user.display_menu()

def handle_add_item_to_menu(user: User, json_data):
    food = Food(
        food_name=json_data["food_name"],
        price=json_data["price"],
        availability_status=True,
        category=json_data["food_type"],
        avg_rating=0,
        feedbacks=[],
        food_type=json_data["food_type"]
    )
    notification = AddItemNotification()
    user.add_item_to_menu(food)
    notification.send_notification(json_data["food_name"])
    return {"status": "success"}


def handle_change_food_price(user: User, json_data):
    return user.change_food_price(json_data["food_name"], json_data["new_price"])


def handle_change_food_availability(user: User, json_data):
    notification = AddItemNotification()
    notification.send_notification(json_data["food_name"])
    return user.change_food_availability(json_data["food_name"], json_data["availability"])


def handle_remove_item_from_menu(user: User, json_data):
    db = DatabaseMethods()
    if not db.food_exists_in_menu(json_data['food_name']):
        return {"response": FoodDoesNotExist(f"Food {json_data['food_name']} doesn't exist")}
    else:
        notification = RemoveItemNotification()
        notification.send_notification(json_data["food_name"])
        user.remove_item_from_menu(json_data["food_name"])
        return {"status": "success"}


def handle_give_feedback(user: User, json_data):
    sentiment_analyzer = RuleBasedSentiment()
    feedback = Feedback(
        food_name=json_data['food_name'],
        comments=json_data['comment'],
        rating=json_data['rating'],
        is_liked=True if json_data['is_liked'] == "Yes" else False,
        user_id=user.user_id,
        sentiment=sentiment_analyzer.get_sentiment(json_data['comment'])['Sentiment']
    )
    return user.give_feedback_on_food(feedback)


def handle_vote(user: User, json_data):
    return user.vote_food_recommended(user.user_id, json_data["food_name"])


def handle_rollout_recommendation(user: User, json_data):
    return user.rollout_food_recommendation(json_data["recommended_food"])


def handle_food_recommendation(user: User, json_data):
    return user.get_food_recommendation()
