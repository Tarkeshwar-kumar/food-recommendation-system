import mysql.connector
import os
from server.model.food import Food
from server.model.feedback import Feedback
class DatabaseConnection:
   def __init__(self):
       self.host = "localhost"
       self.user = "root"
       self.password = "chelsiGoyal@123"
       self.connection = None

   def __enter__(self):
       self.connection = mysql.connector.connect(
           host = self.host,
           user = self.user,
           password = self.password,
           database = "foodApp"
        )
       return self.connection

   def __exit__(self, exc_type, exc_value, traceback):
       if self.connection:
           self.connection.close()

class DatabaseMethods:

    def authenticate(self, user_id: str, password: str):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""SELECT * FROM User WHERE user_id='{user_id}' AND password='{password}';"""
            )
            response = cursor.fetchall()
            print(response)
            role = response[0][3]
            print(role)
            return role

    def get_user_details(self, user_id):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""SELECT user_id, user_name, role FROM User WHERE user_id='{user_id}';"""
            )
            response = cursor.fetchall()
            print(response)
            user_id, user_name, role = response[0][0], response[0][1], response[0][2]
            return user_id, user_name, role

    def insert_item_to_menu(self, food: Food):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            response = cursor.execute(
                f"""
                    INSERT INTO Food (food_name, price, availability_status, avg_rating, food_type, menu_id) VALUES
                    ('{food.food_name}', {food.price}, {food.availability_status}, {food.avg_rating}, '{food.food_type}', 1);
                """
            )
            connection.commit() 
            response = cursor.fetchall()
            print(response)
        
    def update_food_price():
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            response = cursor.execute(
                f"""
                    INSERT INTO menu value ()
                """
            )
            print(response)

    def update_food_availability():
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            response = cursor.execute(
                f"""
                    INSERT INTO menu value ()
                """
            )
            print(response)

    def delete_item_from_menu():
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            response = cursor.execute(
                f"""
                    INSERT INTO menu value ()
                """
            )
            print(response)

    def insert_item_for_recommendation(self, food_name: str):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            response = cursor.execute(
                """
                INSERT INTO RecommendedFood (food_name, total_vote, menu_id)
                VALUES (%s, %s, %s);
                """,
                (food_name, 0, 2)
            )
            connection.commit() 
            response = cursor.fetchall()
            print(response)
            print("Item inserted successfully")

    def food_exists_in_menu(self, food_name) -> bool:
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            response = cursor.execute(
                f"""
                    SELECT * From Food WHERE food_name='{food_name}';
                """
            )
            response = cursor.fetchall()
            print(response)
            if len(response[0]) > 0:
                return True
            return False
    
    def delete_table(self):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""
                    DELETE FROM RecommendedFood;"
                """
            )

    def is_valid_feedback(self, food_name: str, user_id: str):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""
                    SELECT * from Feedback WHERE food_name='{food_name}' and user_id='{user_id}';"
                """
            )
            response = cursor.fetchall()
            print(response)
            if len(response) == 0:
                return True
            return False

    def insert_into_feedback(self, feedback: Feedback):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            print("feedback", feedback)
            cursor.execute(
                """
                INSERT INTO Feedback (message, rating, sentiment, is_liked, user_id, food_name)
                VALUES (%s, %s, %s, %s, %s, %s);
                """,
                (feedback.comments, feedback.rating, feedback.sentiment, feedback.is_liked, feedback.user_id, feedback.food_name)
            )
            connection.commit() 
            print("Item inserted successfully")