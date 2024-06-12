import mysql.connector
import os

class DatabaseConnection:
   def __init__(self):
       self.host = "localhost"
       self.user = os.environ("User")
       self.password = os.environ("PASSWORD")
       self.connection = None

   def __enter__(self):
       self.connection = mysql.connector.connect(
           host = self.host,
           user = self.user,
           password = self.password
        )
       return self.connection

   def __exit__(self, exc_type, exc_value, traceback):
       if self.connection:
           self.connection.close()

class DatabaseMethods:

    def authenticate(user_id: str, password: str):
        with DatabaseConnection() as connection:
            cursor = connection.cursor()
            response = cursor.execute(
                f"""SELECT * FROM User WHERE user_id="{user_id}" AND password="{password}";"""
            )
            print(response)
