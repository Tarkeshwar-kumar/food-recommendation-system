from server.model.users import User
from server.db.db import DatabaseMethods
from server.model.food import Food
from server.model.feedback import Feedback
from server.utils.sentiment import RuleBasedSentiment
from server.model.notification import AddItemNotification, RemoveItemNotification, FoodAvailabilityNotification
from server.exception.exceptions import FoodDoesNotExist, FoodAlreadyExists
from server.utils.handler import *
from server.validators.validation import food_exists_in_menu
from server.auth.auth import Auth


def handle_display_menu(user: User, json_data):
    return user.display_menu()

def handle_add_item_to_menu(user: User, json_data):
        try:
            if food_exists_in_menu(json_data["food_name"]):
                raise FoodAlreadyExists(f"{json_data['food_name']} already exists")

            food = Food(
                food_name=json_data["food_name"],
                price=json_data["price"],
                availability_status=True,
                category=json_data["food_type"],
                avg_rating=0,
                feedbacks=[],
                food_type=json_data["food_type"],
                spice_level=json_data['spice_level'],
                is_sweet=1 if json_data['is_sweet'] == "Yes" else 0,
                region=json_data['is_sweet']
            )
            notification = AddItemNotification()
            user.add_item_to_menu(food)
            notification.send_notification(json_data["food_name"])
            return {"status": "success"}
        except KeyError as e:
            return {"status": "error", "message": f"Missing required field: {str(e)}"}
        except ValueError as e:
            return {"status": "error", "message": f"Invalid value: {str(e)}"}
        except Exception as e:
            return {"status": "error", "message": "An unexpected error occurred: " + str(e)}


def handle_change_food_price(user: User, json_data):
    try:
        db = DatabaseMethods()
        if not db.food_exists_in_menu(json_data['food_name']):
            raise FoodDoesNotExist(f"Food {json_data['food_name']} doesn't exist")
        user.change_food_price(json_data["food_name"], json_data["new_price"])
        return {"status": "success"}
    except FoodDoesNotExist as e:
        return {"status": "error", "message": str(e)}
    except KeyError as e:
        return {"status": "error", "message": f"Missing required field: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": f"An unexpected error occurred: {str(e)}"}


def handle_change_food_availability(user: User, json_data):
    notification = FoodAvailabilityNotification()
    notification.send_notification(json_data["food_name"])
    user.change_food_availability(json_data["food_name"])
    return {"status": "success", "message": "Changed Food Availability"}

def handle_remove_item_from_menu(user: User, json_data):
    try:
        db = DatabaseMethods()
        
        if not db.food_exists_in_menu(json_data['food_name']):
            raise FoodDoesNotExist(f'Food {json_data["food_name"]} doesn\'t exist')

        notification = RemoveItemNotification()
        notification.send_notification(json_data["food_name"])
        user.remove_item_from_menu(json_data["food_name"])
        return {"status": "success", "message": "Food item removed successfully"}

    except FoodDoesNotExist as e:
        return {"status": "error", "message": str(e)}
    except KeyError as e:
        return {"status": "error", "message": f"Missing required field: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": f"An unexpected error occurred: {str(e)}"}


def handle_give_feedback(user: User, json_data):
    db = DatabaseMethods()
    if not db.food_exists_in_menu(json_data['food_name']):
        return {"status": "error", "message": "Food does not exists in the menu."}
    
    if db.have_not_voted(user.user_id, json_data['food_name']):
        return {"status": "error", "message": "User has not voted for this food item."}
    
    if float(json_data['rating']) > 5.0:
        return {"status": "error", "message": "Rating cannot exceed 5"}

    sentiment_analyzer = RuleBasedSentiment()
    feedback = Feedback(
        food_name=json_data['food_name'],
        comments=json_data['comment'],
        rating=json_data['rating'],
        user_id=user.user_id,
        sentiment=sentiment_analyzer.get_sentiment(json_data['comment'])['Sentiment']
    )

    
    if db.is_valid_feedback(json_data['food_name'], user.user_id):
        db.insert_into_feedback(feedback)
        return {"status": "success", "message": "Feedback added successfully."}
    else:
        db.update_feedback(feedback)
        return {"status": "success", "message": "Feedback updated successfully."}



def handle_vote(user: User, json_data):
    return user.vote_food_recommended(user.user_id, json_data["food_name"])


def handle_rollout_recommendation(user: User, json_data):
    return user.rollout_food_recommendation(json_data["recommended_food"])


def handle_food_recommendation(user: User, json_data):
    return user.get_food_recommendation(user.user_id, json_data['limit'])

def handle_check_notification(user: User, json_data):
    db = DatabaseMethods()
    notifications = db.fetch_notifications_for_today(user.user_id)
    notification_list = []
    print("nl", notification_list)
    if notifications:
        for notification in notifications:
            notification_list.append({
                "notification_type": notification["notification_type"],
                "food_name": notification["food_name"]
            })
            db.delete_notification(notification["notification_id"])

    print("nl, ", notification_list)
    return {"notifications": notification_list}

def handle_logout(user: User, json_data):
    auth = Auth()
    auth.logout(user.user_id, json_data['request_type'])


def handle_audit(user: User, json_data):
    return user.audit_food(user, json_data)

def handle_submit_improvement(user: User, json_data):
    return user.submit_improvement_feedback(user.user_id, json_data)

def handle_update_profile(user:User, json_data):
    return user.update_profile(user.user_id, json_data)