import mysql.connector
import os

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

    def insert_item_to_menu():
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            response = cursor.execute(
                f"""
                    INSERT INTO menu value ()
                """
            )
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
